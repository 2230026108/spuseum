// Unpack GLB and extract all textures
const { read, write, Document, TextureInfo, Texture, ExtensionProperty } = require('@gltf-transform/core');
const { NodeIO } = require('@gltf-transform/core');
const fs = require('fs');
const path = require('path');

const io = new NodeIO();

async function main() {
  const doc = await io.read('public/models/airplane/museumvr.glb');
  
  console.log('=== TEXTURES ===');
  const textures = doc.getRoot().listTextures();
  textures.forEach((tex, i) => {
    console.log(`Texture ${i}: name="${tex.getName()}", mimeType="${tex.getMimeType()}", size=${tex.getImage() ? tex.getImage().byteLength : 'N/A'}`);
  });

  console.log('\n=== MESHES ===');
  const meshes = doc.getRoot().listMeshes();
  meshes.forEach((mesh, i) => {
    console.log(`\nMesh ${i}: name="${mesh.getName()}"`);
    const prims = mesh.listPrimitives();
    prims.forEach((prim, j) => {
      const mat = prim.getMaterial();
      if (mat) {
        console.log(`  Prim ${j}: material="${mat.getName()}"`);
        const baseColor = mat.getBaseColorTexture();
        if (baseColor) {
          const tex = baseColor.getTexture();
          console.log(`    BaseColor: texture="${tex ? tex.getName() : '?'}"`);
        }
        const metallicRoughness = mat.getMetallicRoughnessTexture();
        if (metallicRoughness) {
          const tex = metallicRoughness.getTexture();
          console.log(`    MetallicRoughness: texture="${tex ? tex.getName() : '?'}"`);
        }
        const normal = mat.getNormalTexture();
        if (normal) {
          const tex = normal.getTexture();
          console.log(`    Normal: texture="${tex ? tex.getName() : '?'}"`);
        }
      }
    });
  });

  // Extract textures
  console.log('\n=== EXTRACTING TEXTURES ===');
  const outputDir = 'public/models/airplane/textures';
  if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });
  
  textures.forEach((tex, i) => {
    const img = tex.getImage();
    if (img) {
      const mime = tex.getMimeType() || 'image/png';
      const ext = mime === 'image/jpeg' ? '.jpg' : '.png';
      const name = tex.getName() || `texture_${i}`;
      const safeName = name.replace(/[^a-zA-Z0-9_-]/g, '_');
      const filepath = path.join(outputDir, `${safeName}${ext}`);
      fs.writeFileSync(filepath, img);
      console.log(`Extracted: ${filepath} (${img.byteLength} bytes)`);
    }
  });
}

main().catch(console.error);
