from __future__ import annotations

from typing import Any

from .models import StageArtifact, WorkflowState
from .tools import ToolHub


def _clean(items: list[str]) -> list[str]:
    return [item.strip() for item in items if str(item).strip()]


def _section(title: str, body: list[str]) -> str:
    lines = [f"### {title}", ""]
    lines.extend(body)
    return "\\n".join(lines).rstrip()


def _bullet_lines(items: list[str]) -> list[str]:
    return [f"- {item}" for item in _clean(items)]


def _provider_text(stage: str, prompt: str, fallback: str, provider: Any | None) -> str:
    if provider and hasattr(provider, "available") and provider.available():
        try:
            return provider.generate(stage=stage, prompt=prompt, context={"fallback": fallback, "system": "Luna editorial intelligence"}) or fallback
        except Exception:
            return fallback
    return fallback


def intake(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    lines = [
        f"Project: {brief.project_name}",
        f"Topic: {brief.topic}",
        f"Goal: {brief.goal}",
        f"Audience: {brief.audience}",
        f"Primary platform: {brief.primary_platform}",
        f"Tone: {brief.tone or 'premium, clear, editorial'}",
    ]
    if brief.constraints:
        lines.append("Constraints:")
        lines.extend(_bullet_lines(brief.constraints))
    if brief.success_metric:
        lines.append(f"Success metric: {brief.success_metric}")
    fallback = _section("Goal intake", lines)
    body = _provider_text("goal_intake", fallback, fallback, provider)
    return StageArtifact(
        stage="goal_intake",
        specialist="goal_intake",
        summary="Brief normalized into a usable strategy target.",
        payload={"body": body, "goal": brief.goal, "platform": brief.primary_platform},
        prompt=f"Normalize this Luna brief into a strategy target:\n{brief.to_dict()}",
    )


def research(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    memory = state.memory
    plan = tools.research.plan(brief, memory)
    body = _section(
        "Research",
        [
            "Research angles:",
            *_bullet_lines(plan["search_angles"]),
            "",
            "Open questions:",
            *_bullet_lines([
                f"Which proof points turn {brief.audience} from curious to convinced?",
                "What existing narrative already owns this topic?",
                "What source material can be reused across platforms?",
            ]),
            "",
            f"Known context: {plan['known_context'] or 'none loaded yet'}",
        ],
    )
    body = _provider_text("research", body, body, provider)
    return StageArtifact(
        stage="research",
        specialist="research",
        summary="Built the evidence plan and the remaining questions.",
        payload={"body": body, "search_angles": plan["search_angles"]},
        prompt=f"Build the research layer for this Luna brief:\n{brief.to_dict()}\nMemory:\n{memory}",
    )


def audience_synthesis(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    memory = state.memory
    voice = brief.brand_voice or memory.get("brand", {}).get("positioning", "")
    body = _section(
        "Audience synthesis",
        [
            f"Primary audience: {brief.audience}",
            "What they want: faster wins with less guesswork.",
            "What they fear: wasted posts, weak hooks, inconsistent brand voice.",
            f"Language to mirror: {voice or 'clear, premium, direct language'}.",
            "",
            "Behavioral cues:",
            *_bullet_lines([
                "Skims quickly unless the opening claim feels specific.",
                "Stops for proof, contrast, and concrete examples.",
                "Responds to editorial confidence more than hype.",
            ]),
        ],
    )
    body = _provider_text("audience_synthesis", body, body, provider)
    return StageArtifact(
        stage="audience_synthesis",
        specialist="audience",
        summary="Translated the brief into a usable audience profile.",
        payload={"body": body, "language": voice},
        prompt=f"Synthesize the audience for this Luna brief:\n{brief.to_dict()}\nMemory:\n{memory}",
    )


def trends(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    body = _section(
        "Trend intelligence",
        [
            f"Track the angles adjacent to {brief.topic} rather than chasing every trend.",
            "",
            "Trend notes:",
            *_bullet_lines([
                "Editorial systems outperform vague 'post more' advice because they promise repeatability.",
                "Short-form content that names a specific mistake earns more saves than generic inspiration.",
                "Clean before/after framing converts better than abstract brand talk.",
            ]),
            "",
            "Monitoring rule: keep trend coverage narrow, useful, and reusable across the next three posts.",
        ],
    )
    body = _provider_text("trends", body, body, provider)
    return StageArtifact(
        stage="trends",
        specialist="trend_intelligence",
        summary="Captured the trend context that matters for this topic.",
        payload={"body": body, "trend_rule": "narrow, useful, reusable"},
        prompt=f"Analyze the trend context for this Luna brief:\n{brief.to_dict()}",
    )


def positioning(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    body = _section(
        "Positioning",
        [
            f"Positioning statement: Luna is the editorial intelligence layer that turns {brief.topic.lower()} into a repeatable operating system.",
            "",
            "Differentiators:",
            *_bullet_lines([
                "Research becomes a decision tool instead of a loose idea list.",
                "Hooks are evaluated before the draft is expanded.",
                "Brand voice and analytics stay in the loop after publication.",
            ]),
            "",
            f"Category promise: {brief.goal} with less chaos and more signal.",
        ],
    )
    body = _provider_text("positioning", body, body, provider)
    return StageArtifact(
        stage="positioning",
        specialist="positioning",
        summary="Defined Luna's category, promise, and differentiators.",
        payload={"body": body, "promise": brief.goal},
        prompt=f"Create the positioning for this Luna brief:\n{brief.to_dict()}\nMemory:\n{state.memory}",
    )


def hook_generation(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    audience = brief.audience
    topic = brief.topic
    hooks = [
        f"Most {audience} do not need more ideas. They need a content system that turns {topic.lower()} into something publishable.",
        "The fastest way to sharpen a brand is not another brainstorm. It is a cleaner research-to-hook pipeline.",
        "If your content feels random, your audience feels it before they read the caption.",
        "Luna turns research, hooks, and brand voice into one repeatable editorial stack.",
        "The premium content advantage is simple: decide faster, publish cleaner, learn sooner.",
        "Good hooks do not shout. They make the next line impossible to ignore.",
        "Every weak post starts the same way: with vague inputs and too much guessing.",
        "Strategy is what content looks like when the feed stops being a gamble.",
    ]
    best_hook = hooks[0]
    body = _section(
        "Hook engineering",
        [
            "Hook set:",
            *_bullet_lines(hooks),
            "",
            f"Best hook: {best_hook}",
        ],
    )
    body = _provider_text("hook_generation", body, body, provider)
    return StageArtifact(
        stage="hook_generation",
        specialist="hook_engineering",
        summary="Built a hook set with a clear winner.",
        payload={"body": body, "hooks": hooks, "best_hook": best_hook},
        prompt=f"Generate Luna hooks for this brief:\n{brief.to_dict()}\nMemory:\n{state.memory}",
    )


def draft_generation(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    hook = state.previous("hook_generation")
    best_hook = hook.payload.get("best_hook", brief.topic) if hook else brief.topic
    body = _section(
        "Draft generation",
        [
            f"Opening line: {best_hook}",
            "",
            "Structure:",
            *_bullet_lines([
                "State the content problem in one sentence.",
                "Show why the old approach wastes time or weakens the brand.",
                "Introduce Luna as the editorial system that fixes the bottleneck.",
                "Close with a concrete CTA tied to the brief's success metric.",
            ]),
            "",
            f"CTA: {brief.call_to_action or 'download the Luna brief template'}",
        ],
    )
    body = _provider_text("draft_generation", body, body, provider)
    return StageArtifact(
        stage="draft_generation",
        specialist="script_writing",
        summary="Outlined the first-pass draft structure.",
        payload={"body": body, "opening_line": best_hook},
        prompt=f"Draft the content for this Luna brief using the best hook:\n{brief.to_dict()}\nHook:\n{best_hook}",
    )


def review_loop(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    draft = state.previous("draft_generation")
    hook = state.previous("hook_generation")
    draft_text = (draft.payload.get("body", "") if draft else "").lower()
    hook_count = len(hook.payload.get("hooks", [])) if hook else 0
    needs_revision = hook_count < 6 or "generic" in draft_text or len(draft_text) < 120
    notes = [
        "ready to publish" if not needs_revision else "revise the hook or draft before handoff",
        "check for stronger proof if the opening feels abstract",
        "keep the CTA concrete and on-brand",
    ]
    body = _section(
        "Review loop",
        [
            f"Decision: {'revision needed' if needs_revision else 'approved'}",
            "",
            "Review notes:",
            *_bullet_lines(notes),
        ],
    )
    body = _provider_text("review_loop", body, body, provider)
    return StageArtifact(
        stage="review_loop",
        specialist="review",
        summary="Checked the draft against Luna's editorial standards.",
        payload={"body": body, "notes": notes},
        prompt=f"Review this Luna draft for clarity and brand fit:\n{draft.payload if draft else {}}",
        needs_revision=needs_revision,
    )


def revise(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    review = state.previous("review_loop")
    hook = state.previous("hook_generation")
    draft = state.previous("draft_generation")
    hooks = list(hook.payload.get("hooks", [])) if hook else []
    revised_hook = hooks[0] if hooks else state.brief.topic
    if hooks:
        revised_hook = hooks[0].replace("need more ideas", "need a tighter editorial system")
    revised_draft = (draft.payload.get("body", "") if draft else "").replace("generic", "specific")
    body = _section(
        "Revision",
        [
            f"Review status: {review.summary if review else 'none'}",
            "",
            f"Revised hook: {revised_hook}",
            "",
            "Revised draft notes:",
            *_bullet_lines([
                "Trim repetition.",
                "Lead with the cleaner system, not the abstract brand claim.",
                "End with the exact next action.",
            ]),
        ],
    )
    body = _provider_text("revise", body, body, provider)
    payload = {
        "body": body,
        "revised_hook": revised_hook,
        "revised_draft": revised_draft,
        "applies_to": ["hook_generation", "draft_generation"],
    }
    return StageArtifact(
        stage="revise",
        specialist="revision",
        summary="Applied a narrow revision pass when the review loop requests it.",
        payload=payload,
        prompt=f"Revise the Luna hook and draft after this review:\n{review.payload if review else {}}",
    )


def visual_direction(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    body = _section(
        "Visual direction",
        [
            f"Visual system: {brief.visual_style or 'minimal editorial composition with strong hierarchy'}",
            "",
            "Shot guidance:",
            *_bullet_lines([
                "Use close framing on the headline and supporting proof.",
                "Keep the layout clean enough that one idea lands per frame.",
                "Carry the same palette across the reel, carousel, and thumbnail.",
            ]),
            "",
            "Thumbnail rule: one sharp promise, one visual anchor, no clutter.",
        ],
    )
    body = _provider_text("visual_direction", body, body, provider)
    return StageArtifact(
        stage="visual_direction",
        specialist="visual_direction",
        summary="Converted the strategy into visual guidance.",
        payload={"body": body, "style": brief.visual_style},
        prompt=f"Create visual guidance for this Luna brief:\n{brief.to_dict()}",
    )


def seo_metadata(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    hook = state.previous("hook_generation")
    hook_text = hook.payload.get("best_hook", brief.topic) if hook else brief.topic
    keywords = _clean([brief.topic, brief.project_name, brief.primary_platform, "content strategy", "editorial system"] + brief.content_pillars)
    body = _section(
        "SEO metadata",
        [
            f"Title: {hook_text[:90]}",
            f"Slug: {brief.project_name.lower().replace(' ', '-')}-{brief.primary_platform}",
            f"Description: {brief.goal}",
            "",
            "Keywords:",
            *_bullet_lines(keywords),
        ],
    )
    body = _provider_text("seo_metadata", body, body, provider)
    return StageArtifact(
        stage="seo_metadata",
        specialist="seo",
        summary="Packaged the metadata for discoverability.",
        payload={"body": body, "keywords": keywords, "title": hook_text[:90]},
        prompt=f"Write SEO metadata for this Luna brief:\n{brief.to_dict()}",
    )


def distribution_plan(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    brief = state.brief
    hook = state.previous("hook_generation")
    best_hook = hook.payload.get("best_hook", brief.topic) if hook else brief.topic
    platforms = [brief.primary_platform, *brief.secondary_platforms]
    plan = []
    for platform in platforms:
        plan.append(f"{platform}: publish the core post, then cut one derived angle for the next 48 hours.")
    body = _section(
        "Distribution",
        [
            "Channel plan:",
            *_bullet_lines(plan),
            "",
            "Repurposing:",
            *_bullet_lines([
                "Turn the opening hook into a carousel headline.",
                "Turn the strongest proof point into a short clip or quote card.",
                "Reuse the CTA as the closing line in the follow-up post.",
            ]),
            "",
            f"Launch note: keep the first publication centered on '{best_hook}'.",
        ],
    )
    body = _provider_text("distribution_plan", body, body, provider)
    return StageArtifact(
        stage="distribution_plan",
        specialist="distribution",
        summary="Mapped the publication and repurposing plan.",
        payload={"body": body, "platforms": platforms},
        prompt=f"Create a distribution plan for this Luna brief:\n{brief.to_dict()}",
    )


def publication_handoff(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    package = tools.publication.package(state)
    body = _section(
        "Publication handoff",
        [
            f"Title: {package['title']}",
            "",
            "Handoff package:",
            *_bullet_lines([
                "final copy ready for scheduling",
                "SEO metadata attached",
                "visual direction attached",
                "distribution plan attached",
            ]),
            "",
            package["handoff_note"],
        ],
    )
    body = _provider_text("publication_handoff", body, body, provider)
    return StageArtifact(
        stage="publication_handoff",
        specialist="handoff",
        summary="Assembled the package for publish-time use.",
        payload={"body": body, **package},
        prompt=f"Package this Luna run for publication:\n{state.brief.to_dict()}",
    )


def analytics_review(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    feedback = state.analytics_feedback or {}
    analysis = tools.analytics.summarize(feedback)
    metrics = analysis.get("metrics", {})
    body = _section(
        "Analytics review",
        [
            f"Best signal: {analysis.get('best_signal') or 'not provided'}",
            f"Weak signal: {analysis.get('weak_signal') or 'not provided'}",
            "",
            "Metrics:",
            *_bullet_lines([f"{key}: {value}" for key, value in metrics.items()] or ["no metrics supplied"]),
            "",
            "What to change next:",
            *_bullet_lines([
                "Keep the strongest hook pattern.",
                "Move the highest-save proof point earlier.",
                "Reduce any section that repeats the brand claim without adding evidence.",
            ]),
        ],
    )
    body = _provider_text("analytics_review", body, body, provider)
    return StageArtifact(
        stage="analytics_review",
        specialist="analytics",
        summary="Converted performance feedback into strategy notes.",
        payload={"body": body, "analysis": analysis},
        prompt=f"Review analytics for this Luna run:\n{feedback}",
    )


def memory_update(state: WorkflowState, tools: ToolHub, provider: Any | None = None) -> StageArtifact:
    hook = state.previous("hook_generation")
    review = state.previous("review_loop")
    analytics = state.previous("analytics_review")
    memory_patch = {
        "brand": {
            "mission": "Luna turns content chaos into a repeatable operating system.",
            "positioning": "editorial intelligence layer",
            "north_star": "faster research, sharper strategy, better hooks, stronger brand consistency, measurable performance",
        },
        "winning_hooks": hook.payload.get("hooks", [])[:3] if hook else [],
        "failed_hooks": [] if review and not review.needs_revision else ["review requested a revision pass"],
        "analytics": [analytics.payload.get("analysis", {})] if analytics else [],
        "evergreen_ideas": [
            "Research-to-hook workflow as a repeatable operating system",
            "Editorial voice rules for premium faceless brands",
        ],
    }
    body = _section(
        "Memory update",
        [
            "Durable memory patch ready for persistence.",
            "",
            "Stored fields:",
            *_bullet_lines([f"{key}" for key in memory_patch.keys()]),
        ],
    )
    body = _provider_text("memory_update", body, body, provider)
    return StageArtifact(
        stage="memory_update",
        specialist="memory",
        summary="Prepared the durable memory patch for future strategy runs.",
        payload={"body": body, "memory_patch": memory_patch},
        prompt=f"Update Luna memory from this run:\n{state.artifacts.keys()}",
    )


SPECIALISTS = {
    "goal_intake": intake,
    "research": research,
    "audience_synthesis": audience_synthesis,
    "trends": trends,
    "positioning": positioning,
    "hook_generation": hook_generation,
    "draft_generation": draft_generation,
    "review_loop": review_loop,
    "revise": revise,
    "visual_direction": visual_direction,
    "seo_metadata": seo_metadata,
    "distribution_plan": distribution_plan,
    "publication_handoff": publication_handoff,
    "analytics_review": analytics_review,
    "memory_update": memory_update,
}
