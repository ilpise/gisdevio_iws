(self.webpackChunkMyExt=self.webpackChunkMyExt||[]).push([[611],{11611:(e,t,n)=>{"use strict";n.r(t),n.d(t,{default:()=>m});var r=n(84956),i=n.n(r),l=n(88042),o=n.n(l),s=n(44142),c=n.n(s);function a(e){const t={"==":"===",">":">",">=":">=","<":"<","<=":"<=","!=":"!==","*=":"=~"},[n,...r]=e;switch(n){case"||":case"&&":return`(${r.map((e=>a(e))).join(` ${n} `)})`;case">":case"<":case">=":case"<=":case"!=":case"==":case"*=":const[e,i]=r;return function(e,t,n){const r=`!(\${${e}} === undefined${null===n?"":` || \${${e}} === null`})`;return"=~"===t?`(${r} && regExp('${n}').test(\${${e}}) === true)`:`(${r} && \${${e}} ${t} ${o()(n)?`'${n}'`:n})`}(e,t[n],i);default:return""}}function u(e){return!e||a(e)}function f(e){let{conditions:t}=e;return 1===t.length&&!0===t[0][0]?t[0][1]:{conditions:t}}function d(e){if(/rgb\(|rgba\(|hsl\(|hsla\(/.test(e)){const t=c()(e);return{color:t.toHexString(),fillOpacity:t.getAlpha()}}if(/color\(/.test(e)){const[t,n]=e.replace(/color\(|\)/g,"").split(",");return{color:t.replace(/\'/g,""),fillOpacity:parseFloat(void 0!==n?n:1)}}return{color:"#ffffff",fillOpacity:1}}const m=class{readStyle(e){return new Promise(((t,n)=>{try{const n=function(){let{color:e,pointSize:t,meta:n}=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};const r=n?.names?i()(n.names,"'").split(","):[],l=o()(e)?[{filter:void 0,name:r[0]||"",symbolizers:[{kind:t?"Mark":"Fill",...d(e)}]}]:e?.conditions?.map(((e,n)=>{const i=e[1];return{filter:void 0,name:r[n]||"",symbolizers:[{kind:t?"Mark":"Fill",...d(i)}]}}));return{name:n?.title?i()(n.title,"'"):"",rules:[...l].reverse()}}(e);t(n)}catch(e){n(e)}}))}writeStyle(e){return new Promise(((t,n)=>{try{const n=function(){let{name:e,rules:t=[]}=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};const n=[...t].reverse(),r=n.find((e=>{let{symbolizers:t}=e;return"Mark"===t[0].kind})),i=n.map((e=>{let{filter:t,symbolizers:n}=e;return[u(t),r&&0===(n[0].fillOpacity||0)?"${COLOR}":`color('${n[0].color}', ${n[0].fillOpacity})`]})),l=i.find((e=>{let[t]=e;return!0===t})),o=!l&&{show:i.filter((e=>!0!==e)).map((e=>{let[t]=e;return t})).join(" || ")},s=n.map((e=>{let{filter:t,symbolizers:n}=e;return[u(t),n[0].radius||1]})),c=n.map((e=>{let{name:t}=e;return t})),a=!!c.find((e=>!!e));return{...o,color:f({conditions:l?i:[...i,[!0,"color('#ffffff', 1)"]]}),...r&&{pointSize:f({conditions:l?s:[...s,[!0,1]]})},...(e||a)&&{meta:{...e&&{title:`'${e}'`},...a&&{names:`'${c.join(",")}'`}}}}}(e);t(n)}catch(e){n(e)}}))}}}}]);