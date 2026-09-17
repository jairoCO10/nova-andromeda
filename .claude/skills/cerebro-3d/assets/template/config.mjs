import path from 'node:path';
import os from 'node:os';

export const palette = ['#38BDF8','#FB923C','#F472B6','#FBBF24','#67E8F9','#34D399','#A78BFA','#FCA5A5','#A3E635','#C4B5FD','#FDE68A','#94A3B8'];
export function validateConfig(input) {
  if (!input || typeof input !== 'object') throw new Error('La configuración debe ser un objeto.');
  const name = String(input.name || '').trim();
  if (!name || name.length > 64) throw new Error('El nombre del cerebro debe tener entre 1 y 64 caracteres.');
  if (!Array.isArray(input.sources) || !input.sources.length || input.sources.length > 12) throw new Error('Elige entre 1 y 12 categorías.');
  const ids = new Set();
  const sources = input.sources.map((s,i) => {
    if (!/^[a-z][a-z0-9-]{0,39}$/.test(s.id || '') || ids.has(s.id)) throw new Error('Cada categoría necesita un ID único en minúsculas.');
    ids.add(s.id);
    if (typeof s.label !== 'string' || !s.label.trim() || s.label.length > 64) throw new Error(`Etiqueta de categoría inválida: ${s.id}`);
    const type = s.type || 'markdown';
    if (!['markdown','codex-memory'].includes(type)) throw new Error(`Adaptador no compatible: ${type}`);
    if (!Array.isArray(s.paths) || !s.paths.length || s.paths.some((p) => typeof p !== 'string' || !p.trim())) throw new Error(`Indica rutas reales de archivos o carpetas para ${s.label}.`);
    if (s.color && !/^#[0-9a-f]{6}$/i.test(s.color)) throw new Error(`Usa un color hexadecimal de seis dígitos para ${s.label}.`);
    if (s.exclude && (!Array.isArray(s.exclude) || s.exclude.some((p) => typeof p !== 'string'))) throw new Error('exclude debe ser una lista de rutas relativas.');
    const staleDays = s.staleDays === null ? null : Number(s.staleDays ?? 90);
    if (staleDays !== null && (!Number.isFinite(staleDays) || staleDays < 1)) throw new Error('staleDays debe ser un número positivo o null.');
    return {...s, type, color:s.color || palette[i], staleDays, short:s.short || s.label, blurb:s.blurb || `Conocimiento guardado de ${s.label}.`};
  });
  const port = Number(input.port ?? 4640);
  if (!Number.isInteger(port) || port < 1024 || port > 65535) throw new Error('Usa un puerto entre 1024 y 65535.');
  const maxNodes = Number(input.maxNodes ?? 3000);
  if (!Number.isInteger(maxNodes) || maxNodes < 1 || maxNodes > 10000) throw new Error('maxNodes debe estar entre 1 y 10000.');
  return {...input, version:1, name, root:String(input.root || '../..'), port, maxNodes, sources};
}
export function expandPath(value, root) {
  if (value === '~') return os.homedir();
  if (/^~[/\\]/.test(value)) return path.resolve(os.homedir(),value.slice(2));
  return path.resolve(root,value);
}
