// Runs as a next/script beforeInteractive tag in the root layout, before
// hydration -- paints the persisted mode onto <html> immediately so there's
// no flash of light for a user who chose dark (or "system" on a dark device).
// Mirrors the shape zustand's persist middleware writes for the
// "ap-study-app:theme" key (see theme-store.ts); ThemeSync takes over DOM
// sync once React/zustand have actually hydrated. It also drops the
// data-color-theme attribute the retired palette picker used to set.
export const THEME_INIT_SCRIPT = `(function(){try{var raw=localStorage.getItem('ap-study-app:theme');var state=raw?JSON.parse(raw).state:null;var mode=state&&state.mode;var dark=mode==='dark'||(mode==='system'&&window.matchMedia('(prefers-color-scheme: dark)').matches);var root=document.documentElement;if(dark)root.classList.add('dark');root.removeAttribute('data-color-theme');}catch(e){}})();`;
