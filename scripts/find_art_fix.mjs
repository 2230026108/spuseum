import { NodeIO } from '@gltf-transform/core';
import { KHRONOS_EXTENSIONS } from '@gltf-transform/extensions';

const io = new NodeIO().registerExtensions(KHRONOS_EXTENSIONS);
const doc = await io.read('public/models/airplane/museumvr.glb');
const root = doc.getRoot();

const materials = root.listMaterials();
const textures = root.listTextures();

console.log('Textures total:', textures.length);
console.log('Art materials and their textures:\n');

materials.forEach((mat, idx) => {
  const name = mat.getName() || '';
  if (name.toLowerCase().startsWith('art')) {
    // Use the JSON representation
    const json = doc.getRoot().getGraph().toJSON();
    
    // Actually let me try accessing through the doc
    const refs = mat.listTextureInfoRefs ? mat.listTextureInfoRefs() : [];
    console.log(`${name}: refs=${refs.length}`);
    
    // Try getBaseColorTextureInfo
    const info = mat.getBaseColorTextureInfo();
    if (info) {
      // Try to get the link
      const links = mat.listParents ? mat.listParents() : [];
      console.log(`  info type: ${typeof info}, links: ${JSON.stringify(links)}`);
    }
  }
});

// Let me try the GLB raw approach
console.log('\n=== Trying JSON export ===');
import { writeJSON } from '@gltf-transform/core';
// Actually gltf-transform's JSON is the document JSON
const jsonDoc = await io.readJSON('public/models/airplane/museumvr.glb');
