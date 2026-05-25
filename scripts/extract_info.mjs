import { NodeIO } from '@gltf-transform/core';
import fs from 'fs';
import path from 'path';

const io = new NodeIO();
const doc = await io.read('public/models/airplane/museumvr.glb');
const root = doc.getRoot();

console.log('=== TEXTURES ===');
const textures = root.listTextures();
const outDir = 'public/models/airplane/textures';
if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

textures.forEach((tex, i) => {
  const img = tex.getImage();
  console.log(`${i}: name="${tex.getName()}", mime="${tex.getMimeType()}", bytes=${img ? img.byteLength : 0}`);
  
  if (img) {
    const ext = tex.getMimeType() === 'image/jpeg' ? '.jpg' : '.png';
    const safeName = (tex.getName() || 'unnamed').replace(/[^a-zA-Z0-9_-]/g, '_');
    const filepath = path.join(outDir, `tex_${i}_${safeName}${ext}`);
    fs.writeFileSync(filepath, img);
    console.log(`  -> ${filepath}`);
  }
});

console.log('\n=== MESHES ===');
const meshes = root.listMeshes();
meshes.forEach((mesh, mi) => {
  console.log(`\nMesh ${mi}: "${mesh.getName()}" (primitives: ${mesh.listPrimitives().length})`);
  mesh.listPrimitives().forEach((prim, pi) => {
    const mat = prim.getMaterial();
    if (mat) {
      console.log(`  Prim ${pi}: mat="${mat.getName()}"`);
      // Try to access texture link
      const texRef = mat.getBaseColorTexture();
      if (texRef) {
        console.log(`    BaseColorTexture: found`);
        console.log(`    TextureInfo type: ${typeof texRef}`);
        console.log(`    Keys: ${Object.keys(texRef)}`);
        // Try different access patterns
        if (texRef.getTexture) console.log(`    texture name: ${texRef.getTexture().getName()}`);
        else if (texRef.texture) console.log(`    texture: ${texRef.texture}`);
        else {
          // It might be an index or reference
          const link = mat.getBaseColorTextureInfo();
          if (link) {
            console.log(`    TextureInfo: ${JSON.stringify(Object.keys(link))}`);
            const texIdx = link.getTexture ? link.getTexture() : link.texture;
            console.log(`    Texture: ${texIdx}`);
          }
        }
      }
    }
  });
});
