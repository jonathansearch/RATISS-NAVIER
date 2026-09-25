"""Génère demos/eclatement_3d.html : scène Three.js interactive (données embarquées).
Usage : python3 scripts/make_three.py. MIT."""
import json

D = '/home/user/RATISS-NAVIER/demos/'
snaps = json.load(open(D + 'snaps_v03.json'))
serie = [p for p in json.load(open(D + 'v03_NU100.json'))['serie'] if 'CRASH' not in p]
frames = []
for sn in snaps:
    X = sn['X'][::2]
    om = sn['om'][::2]
    frames.append({'t': sn['t'],
                   'X': [[round(v, 3) for v in p] for p in X],
                   'om': [round(v, 2) for v in om]})
data = json.dumps({'frames': frames,
                   'serie': [{'t': p['t'], 'Om': p['Om'], 'C': p['C']} for p in serie]})
print(f'[three] {len(frames)} frames, {len(frames[0]["X"])} pts, {len(data)//1024} Ko')

html = """<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<title>RATISS-NAVIER v0.3 — Éclatement (Three.js)</title>
<style>
body{margin:0;background:#05070d;color:#dfe6f3;font-family:sans-serif;overflow:hidden}
#scene{position:fixed;inset:0}
#ui{position:fixed;left:12px;bottom:12px;background:#0b1220ee;padding:12px 14px;
border-radius:12px;border:1px solid #1e293b;width:300px}
#ui h3{margin:0 0 6px;font-size:15px}
#ui input[type=range]{width:100%}
#stats{position:fixed;right:12px;top:12px;background:#0b1220ee;padding:10px 14px;
border-radius:12px;border:1px solid #1e293b;font-size:13px;line-height:1.7}
#chart{position:fixed;right:12px;bottom:12px;background:#0b1220ee;border-radius:12px;
border:1px solid #1e293b}
button{background:#2563eb;color:#fff;border:0;border-radius:8px;padding:7px 14px;
font-size:14px;cursor:pointer;margin-right:6px}
.row{display:flex;align-items:center;gap:8px;margin-top:8px}
</style>
<script type="importmap">{"imports":{
"three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
"three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"}}</script>
</head><body>
<div id="scene"></div>
<div id="stats">t=<b id="t">0</b><br>Ω=<b id="om">0</b><br>C=<b id="cc">1</b>
<br><span style="color:#888">drag=rotation molette=zoom</span></div>
<div id="ui"><h3>🌊 Éclatement ν/100 (n=3000)</h3>
<div class="row"><button id="play">⏸ pause</button><span id="fr">0/0</span></div>
<input id="slider" type="range" min="0" max="13" value="0" step="1">
<div class="row"><span>couleur = |vorticité|</span></div></div>
<canvas id="chart" width="300" height="120"></canvas>
<script>const DATA = __DATA__;</script>
<script type="module">
import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
const F = DATA.frames, S = DATA.serie;
const scene = new THREE.Scene();
const cam = new THREE.PerspectiveCamera(55, innerWidth/innerHeight, 0.1, 100);
cam.position.set(2, 2, 9);
const ren = new THREE.WebGLRenderer({antialias:true});
ren.setSize(innerWidth, innerHeight);
document.getElementById('scene').appendChild(ren.domElement);
const ctl = new OrbitControls(cam, ren.domElement);
ctl.target.set(2, 2, 2);
const N = F[0].X.length;
const pos = new Float32Array(N*3), col = new Float32Array(N*3);
const geo = new THREE.BufferGeometry();
geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
geo.setAttribute('color', new THREE.BufferAttribute(col, 3));
scene.add(new THREE.Points(geo, new THREE.PointsMaterial({size:0.07, vertexColors:true})));
scene.add(new THREE.BoxHelper(new THREE.Mesh(new THREE.BoxGeometry(4,4,4),
  new THREE.MeshBasicMaterial()), 0x1e293b)).children;
function inferno(x){
  x = Math.min(1, Math.max(0, x));
  const r = Math.min(1, x*2.2), g = Math.max(0, Math.min(1, (x-0.15)*1.6)), b = Math.max(0, 1-x*2.2);
  return [r, g, b*0.9+0.05];
}
let idx = 0, playing = true;
function show(i){
  idx = i;
  const f = F[i];
  for(let k=0;k<N;k++){
    pos[k*3]=f.X[k][0]; pos[k*3+1]=f.X[k][1]; pos[k*3+2]=f.X[k][2];
    const c = inferno(f.om[k]/20);
    col[k*3]=c[0]; col[k*3+1]=c[1]; col[k*3+2]=c[2];
  }
  geo.attributes.position.needsUpdate = true;
  geo.attributes.color.needsUpdate = true;
  let best = S[0];
  for(const p of S){ if(Math.abs(p.t-f.t)<Math.abs(best.t-f.t)) best = p; }
  document.getElementById('t').textContent = f.t.toFixed(2);
  document.getElementById('om').textContent = Math.round(best.Om);
  document.getElementById('cc').textContent = best.C.toFixed(3);
  document.getElementById('fr').textContent = i + '/' + (F.length-1);
  document.getElementById('slider').value = i;
  drawChart(f.t);
}
const cv = document.getElementById('chart'), cx = cv.getContext('2d');
function drawChart(tc){
  cx.clearRect(0,0,300,120);
  const mx = Math.max(...S.map(p=>p.Om));
  cx.strokeStyle='#ef4444'; cx.beginPath();
  S.forEach((p,i)=>{ const x=p.t/2.5*300, y=115-p.Om/mx*105; i?cx.lineTo(x,y):cx.moveTo(x,y); });
  cx.stroke();
  cx.strokeStyle='#22c55e'; cx.beginPath();
  S.forEach((p,i)=>{ const x=p.t/2.5*300, y=115-p.C*105; i?cx.lineTo(x,y):cx.moveTo(x,y); });
  cx.stroke();
  cx.strokeStyle='#fff'; cx.beginPath();
  cx.moveTo(tc/2.5*300,0); cx.lineTo(tc/2.5*300,120); cx.stroke();
}
document.getElementById('play').onclick = e=>{
  playing = !playing; e.target.textContent = playing ? '⏸ pause' : '▶ play';
};
document.getElementById('slider').oninput = e=>{ show(+e.target.value); };
addEventListener('resize', ()=>{
  cam.aspect = innerWidth/innerHeight; cam.updateProjectionMatrix();
  ren.setSize(innerWidth, innerHeight);
});
let last = 0;
function loop(ms){
  requestAnimationFrame(loop);
  if(playing && ms-last > 450){ last = ms; show((idx+1)%F.length); }
  ctl.update(); ren.render(scene, cam);
}
show(0); requestAnimationFrame(loop);
</script></body></html>"""
html = html.replace('__DATA__', data)
open(D + 'eclatement_3d.html', 'w').write(html)
print('[three] html ok')
