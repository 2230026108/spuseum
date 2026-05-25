import { Loader, Sky } from "@react-three/drei";
import { Suspense, useState, useEffect } from "react";
import { StandardReality, LostWorld, Physics  } from "spacesvr";
import { MuseumOverlay } from "../components/MuseumOverlay";
import { MuseumModel } from "../components/MuseumModel";

export default function VrShow () {
    const [modelLoaded, setModelLoaded] = useState(false);
    const [showLoading, setShowLoading] = useState(false);

    useEffect(() => {
      // 延迟显示 loading，避免模型瞬间加载完成时的闪烁
      const timer = setTimeout(() => {
        if (!modelLoaded) setShowLoading(true);
      }, 600);
      return () => clearTimeout(timer);
    }, [modelLoaded]);

    const handleModelReady = () => setModelLoaded(true);

    const playerProps = {
        speed: 1.25,
        controls: {
          disableGyro: true,
        },
      };

      const EnvironmentProps = {
        name: 'Archaeology and Technological Civilization',
      };

    return (
        <div style={{ position: 'relative', width: '100vw', height: '100vh', background: '#030314' }}>
        {/* 加载遮罩 — 在 StandardReality 外面，不受 Canvas 影响 */}
        {showLoading && !modelLoaded && (
          <div className="museum-loading museum-loading--shown">
            <div className="museum-loading__inner">
              <div className="museum-loading__spinner">
                <div className="museum-loading__ring" />
                <div className="museum-loading__ring museum-loading__ring--inner" />
              </div>
              <p className="museum-loading__text">Loading Digital Museum</p>
              <p className="museum-loading__sub">正在加载数字博物馆...</p>
            </div>
          </div>
        )}

        {modelLoaded && (
          <div className="museum-loading museum-loading--shown" style={{ opacity: 0, transition: 'opacity 0.6s', pointerEvents: 'none' }}>
            <div className="museum-loading__inner">
              <div className="museum-loading__spinner">
                <div className="museum-loading__ring" />
                <div className="museum-loading__ring museum-loading__ring--inner" />
              </div>
              <p className="museum-loading__text">Loading Digital Museum</p>
              <p className="museum-loading__sub">正在加载数字博物馆...</p>
            </div>
          </div>
        )}

        <StandardReality playerProps={playerProps} environmentProps={EnvironmentProps}>
            <Sky/>
            <ambientLight/>
            <Suspense fallback={null}>
              <MuseumModelWithCallback onReady={handleModelReady}
                scale={[0.5, 0.5, 0.5]}
                position={[0, 0.3, 0]}
              />
            </Suspense>
        </StandardReality>
        <MuseumOverlay />
      </div>
    )
}

// 包装组件：在 MuseumModel 挂载后通知父组件
function MuseumModelWithCallback({ onReady, ...props }) {
  useEffect(() => {
    // MuseumModel 的 useGLTF 在 Suspense 解析后挂载，此时调用 onReady
    onReady();
  }, [onReady]);
  return <MuseumModel {...props} />;
}
