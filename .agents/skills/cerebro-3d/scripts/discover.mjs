import {promises as fs} from 'node:fs';
import path from 'node:path';
import os from 'node:os';
const at=process.argv.indexOf('--root');
const root=path.resolve(at>=0?process.argv[at+1]:process.cwd());
const candidates=[];
async function add(label,p,type='markdown'){try{const stat=await fs.stat(p);candidates.push({label,path:p,type,isDirectory:stat.isDirectory()});}catch{}}
for(const [label,p] of [['Conocimiento del negocio','context'],['Wiki del negocio','wiki'],['Reuniones','meetings'],['Proyectos','projects'],['Referencias','references'],['Skills','.claude/skills'],['Agentes','.claude/agents']]) await add(label,path.join(root,p));
await add('Memoria de Codex',path.join(process.env.CODEX_HOME||path.join(os.homedir(),'.codex'),'memories'),'codex-memory');
const claude=path.join(os.homedir(),'.claude','projects');
const encoded=root.replace(/[^a-zA-Z0-9]/g,'-').toLowerCase();
try{for(const entry of await fs.readdir(claude,{withFileTypes:true}))if(entry.isDirectory() && entry.name.toLowerCase()===encoded)await add('Memoria de Claude',path.join(claude,entry.name,'memory'));}catch{}
console.log(JSON.stringify({root,candidates,note:'Solo son rutas candidatas. Pregunta al usuario el nombre y las categorías, y confirma qué rutas incluir antes de leer memoria externa. Agrega rutas de categorías personalizadas si hace falta.'},null,2));
