import { useGLTF } from "@react-three/drei";
import { useEffect, useRef } from "react";
import * as THREE from "three";

// 37 张丝绸之路主题画作（#01-#30 古代丝路地点，#31-#37 数字丝路/现代科技）
// 使用 import.meta.env.BASE_URL 让 Vite 构建时自动处理 base 路径
// 本地开发 → '/'，GitHub Pages → './' → 均正确解析
const BASE = import.meta.env.BASE_URL;
const ART = `${BASE}images/artwork/png512/`;
const ARTWORK_PATHS = [
  ART + "artwork_01_changan.png",          // 01 长安 Chang-an
  ART + "artwork_02_yumenguan.png",         // 02 玉门关 Yumen Pass
  ART + "artwork_03_dunhuang.png",          // 03 敦煌莫高窟 Dunhuang Mogao
  ART + "artwork_04_turpan.png",            // 04 吐鲁番 Turpan
  ART + "artwork_05_kashgar.png",           // 05 喀什 Kashgar
  ART + "artwork_06_pamir.png",             // 06 帕米尔高原 Pamir Plateau
  ART + "artwork_07_samarkand.png",         // 07 撒马尔罕 Samarkand
  ART + "artwork_08_bukhara.png",           // 08 布哈拉 Bukhara
  ART + "artwork_09_persian_bazaar.png",    // 09 波斯集市 Persian Bazaar
  ART + "artwork_10_baghdad.png",           // 10 巴格达 Baghdad
  ART + "artwork_11_constantinople.png",    // 11 君士坦丁堡 Constantinople
  ART + "artwork_12_venice.png",            // 12 威尼斯 Venice
  ART + "artwork_13_guangzhou.png",         // 13 广州港 Guangzhou Port
  ART + "artwork_14_zhenghe.png",           // 14 郑和下西洋 Zheng He
  ART + "artwork_15_silk_production.png",   // 15 丝绸生产 Silk Production
  ART + "artwork_16_night_caravan.png",     // 16 夜间商队 Night Caravan
  ART + "artwork_17_buddhism.png",          // 17 佛教传播 Buddhism Spread
  ART + "artwork_18_trade_goods.png",       // 18 贸易货物 Trade Goods
  ART + "artwork_19_indian_ocean.png",      // 19 印度洋 Indian Ocean
  ART + "artwork_20_tea_horse_road.png",    // 20 茶马古道 Tea Horse Road
  ART + "artwork_21_mongol_steppe.png",     // 21 蒙古草原 Mongol Steppe
  ART + "artwork_22_dunhuang_murals.png",   // 22 敦煌壁画 Dunhuang Murals
  ART + "artwork_23_astronomy.png",         // 23 古代天文 Ancient Astronomy
  ART + "artwork_24_tang_capital.png",      // 24 唐朝都城 Tang Capital
  ART + "artwork_25_alexandria.png",        // 25 亚历山大港 Alexandria
  ART + "artwork_26_ancient_rome.png",      // 26 古罗马 Ancient Rome
  ART + "artwork_27_zhang_qian.png",        // 27 张骞出使 Zhang Qian
  ART + "artwork_28_full_map.png",          // 28 丝路全图 Full Silk Road Map
  ART + "artwork_29_marco_polo.png",        // 29 马可·波罗 Marco Polo
  ART + "artwork_30_cultural_fusion.png",   // 30 文化融合 Cultural Fusion
  ART + "artwork_31_belt_road.png",         // 31 一带一路 Belt and Road
  ART + "artwork_32_undersea_cables.png",   // 32 海底电缆 Undersea Cables
  ART + "artwork_33_ecommerce.png",         // 33 全球电商 Global E-Commerce
  ART + "artwork_34_5g_ai.png",             // 34 5G与AI 5G and AI
  ART + "artwork_35_digital_heritage.png",  // 35 数字文化遗产 Digital Heritage
  ART + "artwork_36_digital_connection.png",// 36 数字连接 Digital Connections
  ART + "artwork_37_then_and_now.png",      // 37 古今对比 Then and Now
];

const MODEL_PATH = import.meta.env.BASE_URL + "models/airplane/museumvr.glb";

export function MuseumModel(props) {
  const { scene } = useGLTF(MODEL_PATH);
  const appliedRef = useRef(false);

  useEffect(() => {
    if (appliedRef.current) return;

    // 收集所有画作 mesh（只取叶子节点——真正带材质的那一层）
    const artMeshes = [];
    scene.traverse((child) => {
      if (!child.isMesh) return;
      const name = (child.name || "").toLowerCase();
      // 名字里有 art_work 但排除 frame；只匹配带纹理的叶子 mesh
      if (name.includes("art_work_") && !name.includes("frame") && child.material) {
        const match = name.match(/art_work_(\d+)/);
        const num = match ? parseInt(match[1]) : 0;
        artMeshes.push({ mesh: child, num, name: child.name });
      }
    });

    artMeshes.sort((a, b) => a.num - b.num);
    console.log(`[MuseumModel] Found ${artMeshes.length} artwork meshes, loading textures...`);
    appliedRef.current = true;

    // 不再用 setTimeout 延迟——改用分批次渐进加载避免卡顿
    const loader = new THREE.TextureLoader();
    let loadIndex = 0;
    const BATCH = 6;   // 每批 6 张
    const DELAY = 200;  // 批间间隔 200ms

    function loadBatch() {
      const end = Math.min(loadIndex + BATCH, artMeshes.length);
      for (let i = loadIndex; i < end; i++) {
        const item = artMeshes[i];
        const path = ARTWORK_PATHS[i];
        if (!path) continue;

        // 闭包捕获 item
        const targetMesh = item.mesh;

        loader.load(
          path,
          (tex) => {
            tex.colorSpace = THREE.SRGBColorSpace;
            tex.flipY = true;
            tex.wrapS = THREE.ClampToEdgeWrapping;
            tex.wrapT = THREE.ClampToEdgeWrapping;
            tex.minFilter = THREE.LinearFilter;
            tex.magFilter = THREE.LinearFilter;
            tex.needsUpdate = true;

            // BUGFIX: 使用 targetMesh 而不是未定义的 mesh 变量
            targetMesh.material = new THREE.MeshBasicMaterial({
              map: tex,
              side: THREE.FrontSide,
            });

            console.log(`[MuseumModel] ✓ #${String(i + 1).padStart(2, "0")} ${item.name}`);
          },
          undefined,
          (err) => {
            console.warn(`[MuseumModel] ✗ #${i + 1} ${item.name}:`, err.message);
          }
        );
      }
      loadIndex = end;
      if (loadIndex < artMeshes.length) {
        setTimeout(loadBatch, DELAY);
      } else {
        console.log(`[MuseumModel] All ${artMeshes.length} artwork textures loaded.`);
      }
    }

    const timer = setTimeout(loadBatch, 500);
    return () => clearTimeout(timer);
  }, [scene]);

  return <primitive object={scene} {...props} />;
}


// 不再预加载 GLB —— 避免在 SlideShow 入场时阻塞
// useGLTF.preload(MODEL_PATH);
