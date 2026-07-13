# Pace — Activity App Prototype

A fully interactive prototype of **Pace**, imported from the Claude Design project
*"Pace Activity App Prototype"* and implemented as a self-contained local web app.

Pace is a mobile fitness/activity concept covering onboarding, a home dashboard,
workout discovery ("Move"), search + filters, workout detail & guided session,
activity recording, progress/summary with goals, a social feed, friends, shared
goals, notifications, break mode, and more.

## Run it

Any static file server works — but it must be served over HTTP (opening
`index.html` via `file://` will not work because the runtime fetches sibling files).

```bash
cd "$(dirname "$0")"
python3 -m http.server 8712
# then open http://localhost:8712/index.html
```

The app starts on the splash screen and flows into onboarding. It's a phone
mockup — click through it like a real device.

## What's here

| File | Purpose |
|------|---------|
| `index.html` | **Entry point.** The design template + logic, with React preloaded locally so it runs fully offline. |
| `Pace App.dc.html` | The original Claude Design source (`.dc.html`) exactly as exported. Loads React from a CDN at runtime (needs internet). |
| `support.js` | The Claude Design runtime — compiles the `<x-dc>` template + `<script type="text/x-dc">` logic and renders it with React. |
| `icon-data.js` | UI icons as inline SVG data URIs (`window.PACE_ICONS`). |
| `vendor/` | React 18.3.1 + ReactDOM UMD builds (local, for offline use). |
| `assets/` | Avatars, device logos, the Pace logo, and workout photos. |

### How it works
`index.html` contains a declarative template (`{{ }}` bindings, `<sc-if>`,
`<sc-for>`) and a React component class (`extends DCLogic`) holding all state and
handlers. `support.js` wires the two together. To edit behavior, edit the
`<script type="text/x-dc" data-dc-script>` block; to edit layout, edit the markup
inside `<x-dc>`.

## Note on images

All photos are the full-resolution originals from the design project, downscaled
to display size (long side 1100px for workout photos, 320px for avatars) with EXIF
orientation applied and metadata stripped. The device logos and Pace logo are the
original SVGs. To swap any image, drop a replacement into `assets/` under the same
filename — see the app markup for where each is used.
