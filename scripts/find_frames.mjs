import { NodeIO } from '@gltf-transform/core';

const io = new NodeIO();
const doc = await io.read('public/models/airplane/museumvr.glb');
const root = doc.getRoot();

console.log('=== MESHES with TEXTURES (looking for frame/picture/wall meshes) ===');
const meshes = root.listMeshes();
const textures = root.listTextures();

meshes.forEach((mesh, mi) => {
  const meshName = (mesh.getName() || '').toLowerCase();
  // Only show meshes that might be related to frames/pictures/walls
  if (meshName.includes('frame') || meshName.includes('pic') || meshName.includes('paint') || 
      meshName.includes('wall') || meshName.includes('image') || meshName.includes('art') ||
      meshName.includes('canvas') || meshName.includes('poster') || meshName.includes('display') ||
      meshName.includes('artwork')) {
    
    console.log(`\nMesh ${mi}: "${mesh.getName()}"`);
    mesh.listPrimitives().forEach((prim, pi) => {
      const mat = prim.getMaterial();
      if (mat) {
        const bcTex = mat.getBaseColorTexture();
        if (bcTex) {
          // texIndex is the index into the textures array
          const tex = textures[bcTex];
          const texName = tex ? tex.getName() : '?';
          const texSize = tex && tex.getImage() ? tex.getImage().byteLength : 0;
          console.log(`  Prim ${pi}: mat="${mat.getName()}", texIdx=${bcTex}, texName="${texName}", texSize=${texSize}`);
        } else {
          console.log(`  Prim ${pi}: mat="${mat.getName()}" (no baseColorTexture)`);
        }
      }
    });
  }
});

// Also list all materials with their texture assignments
console.log('\n=== ALL MATERIALS with texture indices ===');
const materials = root.listMaterials();
materials.forEach((mat, mi) => {
  const bcTex = mat.getBaseColorTexture();
  if (bcTex !== null && bcTex !== undefined) {
    console.log(`Material ${mi}: "${mat.getName()}" -> texIdx=${bcTex}`);
  }
});
