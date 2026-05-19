# Design

## Visual Theme

Restrained product UI with cool neutrals, a single indigo-led accent family, and soft layered surfaces that work in both light and dark mode.

## Color

- Backgrounds: tinted slate neutrals, never pure black or white.
- Accent: indigo for primary actions and focus states.
- Supporting accents: teal for success-like emphasis, muted violet for secondary detail.
- States: hover, focus, active, selected, disabled, and empty states should be explicit and consistent.

## Typography

- Use Inter or system-ui for the full interface.
- Use a fixed scale with clear weight contrast.
- Keep body copy readable and concise.

## Components

- Top navigation with a theme toggle.
- Surface panels with subtle borders and soft shadows.
- Rounded primary and secondary buttons.
- Search input with clear focus state.
- Metric bars and compact chart containers.

## Layout

- Sticky top bar, then a single content column with predictable section spacing.
- Responsive grids for type cards and detail panels.
- Avoid decorative containers that do not help scanability.

## Motion

- Short transitions only, around 150 to 220 ms.
- Motion should signal state changes, not page choreography.

## Notes

- Avoid gradient text, default glassmorphism, and left-border accents.
- Keep the light and dark themes visually balanced, not inverted copies of each other.
