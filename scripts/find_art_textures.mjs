import { NodeIO } from '@gltf-transform/core';
import fs from 'fs';

const io = new NodeIO();
const doc = await io.read('public/models/airplane/museumvr.glb');
const root = doc.getRoot();

console.log('=== ART MATERIALS with texture indices ===');
const materials = root.listMaterials();
const textures = root.listTextures();

materials.forEach((mat, mi) => {
  const name = (mat.getName() || '').toLowerCase();
  if (name.startsWith('art')) {
    const bcTexIdx = mat.getBaseColorTexture();
    console.log(`"${mat.getName()}": texIdx=${bcTexIdx}, texType=${typeof bcTexIdx}`);
  }
});

// Now let's try to get a different API
console.log('\n=== Using listTextures approach ===');
materials.forEach((mat, mi) => {
  const name = (mat.getName() || '').toLowerCase();
  if (name.startsWith('art')) {
    const texInfo = mat.getBaseColorTextureInfo();
    if (texInfo) {
      // Try to access the texture property directly
      const graph = texInfo.getGraph ? 'has graph' : 'no graph';
      console.log(`"${mat.getName()}": texInfo keys=${Object.keys(texInfo).join(',')}, graph=${graph}`);
      // The TextureInfo has a 'link' or 'index' that references the texture
      // Let me try: texInfo.listProperties or similar
    }
  }
});

// Third attempt - use doc's JSON
console.log('\n=== Raw JSON for Art materials ===');
// Write the doc to gltf format so we can read the JSON
await io.write('public/models/airplane/museumvr_debug.gltf', doc);
console.log('Wrote debug gltf');

// Read the JSON
const gltfJson = JSON.parse(fs.readFileSync('public/models/airplane/museumvr.gltf', 'utf-8'));

// Find materials that start with Art
console.log('\nArt material texture indices from JSON:');
if (gltfJson.materials) {
  gltfJson.materials.forEach((mat, idx) => {
    if (mat.name && mat.name.startsWith('Art')) {
      const texIdx = mat.pbrMetallicRoughness?.baseColorTexture?.index;
      console.log(`  Material ${idx}: ${mat.name} -> texIdx=${texIdx}`);
    }
  });
}
