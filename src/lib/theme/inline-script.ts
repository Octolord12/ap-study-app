// Runs as a next/script beforeInteractive tag in the root layout, before
// hydration -- paints the persisted theme onto <html> immediately so there's
// no flash of the default (light, fresh-mint) theme for a user who chose
// dark mode or a different color theme. Mirrors the shape zustand's persist
// middleware writes for the "ap-study-app:theme" key (see theme-store.ts);
// ThemeSync takes over DOM sync once React/zustand have actually hydrated.
export const THEME_INIT_SCRIPT = `(function(){try{var raw=localStorage.getItem('ap-study-app:theme');var state=raw?JSON.parse(raw).state:null;var mode=state&&state.mode==='dark'?'dark':'light';var theme=state&&state.colorTheme?state.colorTheme:'fresh-mint';var root=document.documentElement;if(mode==='dark')root.classList.add('dark');if(theme!=='fresh-mint')root.setAttribute('data-color-theme',theme);}catch(e){}})();`;
