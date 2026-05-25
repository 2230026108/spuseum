const { NodeIO } = require('@gltf-transform/core');
const fs = require('fs');
const path = require('path');

async function main() {
  const io = new NodeIO();
  const doc = await io.read('public/models/airplane/museumvr.glb');
  const root = doc.getRoot();
  
  console.log('=== TEXTURES ===');
  const textures = root.listTextures();
  textures.forEach((tex, i) => {
    const img = tex.getImage();
    console.log(`${i}: name="${tex.getName()}", mime="${tex.getMimeType()}", bytes=${img ? img.byteLength : 0}`);
  });

  console.log('\n=== MESHES ===');
  const meshes = root.listMeshes();
  meshes.forEach((mesh, mi) => {
    console.log(`Mesh ${mi}: "${mesh.getName()}"`);
    const prims = mesh.listPrimitives();
    prims.forEach((prim, pi) => {
      const mat = prim.getMaterial();
      if (mat) {
        const bcInfo = mat.getBaseColorTextureInfo();
        if (bcInfo) {
          console.log(`  Prim ${pi}: material="${mat.getName()}", tex="${bcInfo.getTexture()?.getName()}"`);
        }
      }
    });
  });

  // Write to gltf
  console.log('\n=== Converting to glTF ===');
  await io.write('public/models/airplane/museumvr.gltf', doc);
  console.log('Wrote museumvr.gltf');
}

main().catch(e => { console.error(e); process.exit(1); });
