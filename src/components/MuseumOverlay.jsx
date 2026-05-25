import { useState } from 'react';

const frames = [
  {
    id: 1,
    title: "研究方向",
    image: "./images/exhibition/frame1.svg",
    description: "专业：考古学 | 主题：技术文明",
    details: "聚焦：丝绸之路时代 → 当代全球化",
    keywords: "跨文明交流 · 数字丝绸之路 · 文化遗产",
    historical: "丝绸之路在过去连接了各大文明，而今天，技术正在世界范围内创造新的连接。",
    modern: "本项目探索这两种连接方式之间的关系。"
  },
  {
    id: 2,
    title: "为什么选择这个AI工具？",
    image: "./images/exhibition/frame2.svg",
    description: "使用工具：即梦AI视频生成 | 电影级叙事",
    details: "通过AI重建，可视化那些原本无法呈现的历史场景",
    keywords: "AI视频生成 · 数字重建 · 历史可视化",
    historical: "AI工具使我们能够可视化和重建那些过去无法描绘的历史场景。",
    modern: "技术不仅在研究历史，更在激活历史。"
  },
  {
    id: 3,
    title: "为什么选择这些历史时期？",
    image: "./images/exhibition/frame3.svg",
    description: "古丝绸之路 → 数字丝绸之路",
    details: "跨越时空连接文明",
    keywords: "古丝路驼队 · 现代互联网网络",
    historical: "丝绸之路不是单一的道路，而是连接中国、中亚、中东和欧洲的文化交流网络。",
    modern: "今天，我们通过AI、数字平台和全球网络在线交换信息。"
  },
  {
    id: 4,
    title: "历史的十字路口",
    image: "./images/exhibition/frame4.svg",
    description: "佛教石窟壁画 · 丝绸贸易 · 伊斯兰-中国文化交流",
    details: "佛教从印度传入中国。中国丝绸西行远销。",
    keywords: "佛教 · 丝绸贸易 · 伊斯兰文明 · 中华文化",
    historical: "文明在交流中发展——宗教、艺术、贸易和知识都在丝绸之路上流动。",
    modern: "考古学帮助我们发掘和理解这些丰富的跨文化联系。"
  },
  {
    id: 5,
    title: "现代考古视角",
    image: "./images/exhibition/frame5.svg",
    description: "3D扫描 · 无人机测绘 · 数字重建",
    details: "技术帮助文明重新连接。",
    keywords: "3D扫描 · VR保护 · 无人机测绘 · 数字考古",
    historical: "考古学不是为了寻找宝藏，而是为了寻找知识。",
    modern: "3D扫描保存文物。无人机测绘揭示隐藏的地貌。"
  },
  {
    id: 6,
    title: "AI与考古学",
    image: "./images/exhibition/frame6.svg",
    description: "人工智能分析 · 考古数据挖掘",
    details: "AI帮助考古学家发现隐藏的模式。",
    keywords: "AI分析 · 数据挖掘 · 数字遗产 · 模式识别",
    historical: "技术通过揭示曾经不可见的事物，加深了我们对历史的理解。",
    modern: "AI分析揭示了古代数据中隐藏的模式。"
  },
  {
    id: 7,
    title: "今天这意味着什么？",
    image: "./images/exhibition/frame7.svg",
    description: "VR博物馆 · 数字展览 · 在线档案",
    details: "数字技术让人们重新与历史建立联系。",
    keywords: "VR博物馆 · 数字展览 · 全球可及性 · 文化遗产",
    historical: "许多年轻人与传统历史的联系正在减弱。",
    modern: "数字档案打破了地理障碍，使全世界都能接触到人类共同的过往。"
  },
  {
    id: 8,
    title: "结论",
    image: "./images/exhibition/frame8.svg",
    video: "./video/assignment2.mp4",
    description: "古丝绸之路正在转变为数字网络",
    details: "技术正在成为连接文明的新桥梁。",
    keywords: "数字丝绸之路 · 技术文明 · 全球连接",
    historical: "丝绸之路在过去连接了文明。",
    modern: "技术在今天连接着文明。它不是在取代考古学——而是在赋予考古学新的生命。"
  }
];

export const MuseumOverlay = () => {
  const [activeFrame, setActiveFrame] = useState(null);
  const [showMap, setShowMap] = useState(false);
  const [showVideo, setShowVideo] = useState(false);

  return (
    <>
      {/* Museum Title Banner */}
      <div className="museum-banner">
        <h2>考古学与技术文明</h2>
        <p>技术如何重新连接文明</p>
      </div>

      {/* Video Demo Button */}
      <button 
        className={`video-btn ${showVideo ? 'active' : ''}`}
        onClick={() => setShowVideo(!showVideo)}
      >
        {showVideo ? '关闭视频' : '🎬 AI演示视频'}
      </button>

      {/* Silk Road Map Large Display Button */}
      <button 
        className={`silk-road-btn ${showMap ? 'active' : ''}`}
        onClick={() => setShowMap(!showMap)}
      >
        {showMap ? '关闭地图' : '🗺️ 丝绸之路'}
      </button>

      {/* Video Overlay */}
      {showVideo && (
        <div className="video-overlay" onClick={() => setShowVideo(false)}>
          <div className="video-content" onClick={e => e.stopPropagation()}>
            <button className="video-close" onClick={() => setShowVideo(false)}>✕</button>
            <h3>🎬 考古学与技术文明 — AI生成演示</h3>
            <div className="video-player-wrapper">
              <video
                className="video-player"
                src="./video/assignment2.mp4"
                controls
                autoPlay
                playsInline
                preload="metadata"
              />
            </div>
            <p className="video-desc">
              通过即梦AI生成的视频，展现从古丝绸之路到数字丝绸之路的文明连接之旅。
            </p>
          </div>
        </div>
      )}

      {/* Silk Road Map Overlay */}
      {showMap && (
        <div className="silk-road-map-overlay" onClick={() => setShowMap(false)}>
          <div className="silk-road-map-content" onClick={e => e.stopPropagation()}>
            <h3>丝绸之路</h3>
            <img 
              src="./images/exhibition/silkroad.svg" 
              alt="丝绸之路地图" 
              className="silk-road-img"
            />
            <p className="silk-road-desc">
              丝绸之路连接了中国、中亚、中东和欧洲，
              是历史上最重要的贸易、文化和知识交流网络之一。
            </p>
          </div>
        </div>
      )}

      {/* Frame Navigation Menu */}
      <div className="frame-nav">
        <h4>展览画框</h4>
        <div className="frame-nav-buttons">
          {frames.map((frame) => (
            <button
              key={frame.id}
              className={`frame-nav-btn ${activeFrame?.id === frame.id ? 'active' : ''}`}
              onClick={() => setActiveFrame(activeFrame?.id === frame.id ? null : frame)}
            >
              <span className="frame-num">{frame.id}</span>
              <span className="frame-title-small">{frame.title}</span>
            </button>
          ))}
        </div>
      </div>

      {/* Active Frame Detail Overlay */}
      {activeFrame && (
        <div className="frame-detail-overlay" onClick={() => setActiveFrame(null)}>
          <div className="frame-detail-content" onClick={e => e.stopPropagation()}>
            <button className="frame-detail-close" onClick={() => setActiveFrame(null)}>✕</button>
            <div className="frame-detail-header">
              <span className="frame-number">画框 {activeFrame.id}</span>
              <h2>{activeFrame.title}</h2>
            </div>
            <div className="frame-detail-body">
              <div className="frame-detail-image">
                <img src={activeFrame.image} alt={activeFrame.title} />
                {activeFrame.video && (
                  <div className="frame-video-section">
                    <h4>🎬 AI演示视频</h4>
                    <video
                      className="frame-video"
                      src={activeFrame.video}
                      controls
                      playsInline
                      preload="metadata"
                    />
                  </div>
                )}
              </div>
              <div className="frame-detail-text">
                <p className="frame-desc">{activeFrame.description}</p>
                <p className="frame-details">{activeFrame.details}</p>
                <div className="frame-keywords">
                  <strong>关键词：</strong> {activeFrame.keywords}
                </div>
                <div className="frame-historical">
                  <strong>历史意义：</strong>
                  <p>{activeFrame.historical}</p>
                </div>
                <div className="frame-modern">
                  <strong>现代启示：</strong>
                  <p>{activeFrame.modern}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      )}

      <style>{`
        .museum-banner {
          position: fixed;
          top: 20px;
          left: 50%;
          transform: translateX(-50%);
          z-index: 1000;
          text-align: center;
          pointer-events: none;
        }
        .museum-banner h2 {
          font-family: 'DM Serif Display', serif;
          font-size: 1.8rem;
          color: #fff;
          text-shadow: 0 2px 20px rgba(0,0,0,0.7);
          margin: 0;
          letter-spacing: 0.08rem;
        }
        .museum-banner p {
          font-family: 'Inter', sans-serif;
          font-size: 0.9rem;
          color: rgba(255,255,255,0.8);
          text-shadow: 0 1px 10px rgba(0,0,0,0.5);
          margin: 5px 0 0 0;
        }

        .video-btn {
          position: fixed;
          top: 100px;
          right: 20px;
          z-index: 1002;
          padding: 10px 20px;
          background: rgba(180, 50, 50, 0.8);
          border: 2px solid rgba(255,255,255,0.3);
          color: #fff;
          font-family: 'DM Serif Display', serif;
          font-size: 1rem;
          border-radius: 30px;
          cursor: pointer;
          backdrop-filter: blur(10px);
          transition: all 0.3s ease;
        }
        .video-btn:hover {
          background: rgba(200, 60, 60, 1);
          border-color: #fff;
          transform: scale(1.05);
        }
        .video-btn.active {
          background: rgba(53, 53, 204, 0.8);
        }

        .silk-road-btn {
          position: fixed;
          top: 150px;
          right: 20px;
          z-index: 1001;
          padding: 10px 20px;
          background: rgba(53, 53, 204, 0.8);
          border: 2px solid rgba(255,255,255,0.3);
          color: #fff;
          font-family: 'DM Serif Display', serif;
          font-size: 1rem;
          border-radius: 30px;
          cursor: pointer;
          backdrop-filter: blur(10px);
          transition: all 0.3s ease;
        }
        .silk-road-btn:hover {
          background: rgba(53, 53, 204, 1);
          border-color: #fff;
          transform: scale(1.05);
        }
        .silk-road-btn.active {
          background: rgba(200, 50, 50, 0.8);
        }

        .silk-road-map-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0,0,0,0.7);
          z-index: 2000;
          display: flex;
          align-items: center;
          justify-content: center;
          animation: fadeIn 0.3s ease;
        }
        .silk-road-map-content {
          background: rgba(20, 20, 50, 0.95);
          border: 2px solid rgba(201, 168, 76, 0.5);
          border-radius: 16px;
          padding: 30px;
          max-width: 750px;
          width: 92%;
          text-align: center;
          backdrop-filter: blur(20px);
        }
        .silk-road-map-content h3 {
          font-family: 'DM Serif Display', serif;
          font-size: 2rem;
          color: #f0d78c;
          margin: 0 0 20px 0;
        }
        .silk-road-img {
          max-width: 100%;
          height: auto;
          border-radius: 8px;
          margin-bottom: 15px;
        }
        .silk-road-svg {
          max-width: 100%;
          margin-bottom: 15px;
        }
        .silk-road-svg svg {
          width: 100%;
          height: auto;
          border-radius: 8px;
        }
        .silk-road-desc {
          font-family: 'Inter', sans-serif;
          color: rgba(255,255,255,0.85);
          font-size: 0.95rem;
          line-height: 1.8;
          max-width: 500px;
          margin: 0 auto;
        }

        /* Video overlay */
        .video-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0,0,0,0.75);
          z-index: 2001;
          display: flex;
          align-items: center;
          justify-content: center;
          animation: fadeIn 0.3s ease;
        }
        .video-content {
          background: rgba(20, 20, 50, 0.95);
          border: 2px solid rgba(201, 168, 76, 0.5);
          border-radius: 16px;
          padding: 25px 30px;
          max-width: 820px;
          width: 92%;
          text-align: center;
          position: relative;
          backdrop-filter: blur(20px);
        }
        .video-close {
          position: absolute;
          top: 12px;
          right: 15px;
          background: none;
          border: none;
          color: #fff;
          font-size: 1.5rem;
          cursor: pointer;
          opacity: 0.7;
          transition: opacity 0.3s;
          z-index: 10;
        }
        .video-close:hover { opacity: 1; }
        .video-content h3 {
          font-family: 'DM Serif Display', serif;
          font-size: 1.5rem;
          color: #f0d78c;
          margin: 0 0 18px 0;
        }
        .video-player-wrapper {
          background: #000;
          border-radius: 10px;
          overflow: hidden;
          margin-bottom: 12px;
        }
        .video-player {
          width: 100%;
          max-height: 55vh;
          display: block;
          border-radius: 10px;
        }
        .video-desc {
          font-family: 'Inter', sans-serif;
          color: rgba(255,255,255,0.75);
          font-size: 0.85rem;
          line-height: 1.6;
          margin: 0;
        }

        /* Frame video section */
        .frame-video-section {
          margin-top: 15px;
          padding-top: 12px;
          border-top: 1px solid rgba(201,168,76,0.3);
        }
        .frame-video-section h4 {
          font-family: 'DM Serif Display', serif;
          font-size: 0.95rem;
          color: #f0d78c;
          margin: 0 0 8px 0;
        }
        .frame-video {
          width: 100%;
          border-radius: 8px;
          background: #000;
        }

        .frame-nav {
          position: fixed;
          bottom: 20px;
          left: 50%;
          transform: translateX(-50%);
          z-index: 1001;
          text-align: center;
        }
        .frame-nav h4 {
          font-family: 'DM Serif Display', serif;
          color: rgba(255,255,255,0.8);
          font-size: 0.85rem;
          margin: 0 0 8px 0;
          text-shadow: 0 1px 10px rgba(0,0,0,0.5);
        }
        .frame-nav-buttons {
          display: flex;
          gap: 6px;
          flex-wrap: wrap;
          justify-content: center;
        }
        .frame-nav-btn {
          padding: 6px 12px;
          background: rgba(0,0,0,0.5);
          border: 1px solid rgba(255,255,255,0.2);
          color: rgba(255,255,255,0.7);
          font-family: 'Inter', sans-serif;
          font-size: 0.75rem;
          border-radius: 20px;
          cursor: pointer;
          transition: all 0.3s ease;
          display: flex;
          align-items: center;
          gap: 5px;
          backdrop-filter: blur(5px);
        }
        .frame-nav-btn:hover, .frame-nav-btn.active {
          background: rgba(53, 53, 204, 0.7);
          border-color: rgba(255,255,255,0.5);
          color: #fff;
        }
        .frame-num {
          background: #d4a853;
          color: #000;
          width: 20px;
          height: 20px;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          font-size: 0.7rem;
          font-weight: bold;
          flex-shrink: 0;
        }

        .frame-detail-overlay {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background: rgba(0,0,0,0.7);
          z-index: 2000;
          display: flex;
          align-items: center;
          justify-content: center;
          animation: fadeIn 0.3s ease;
        }
        .frame-detail-content {
          background: rgba(20, 20, 50, 0.95);
          border: 2px solid rgba(201, 168, 76, 0.5);
          border-radius: 16px;
          padding: 25px;
          max-width: 650px;
          width: 90%;
          max-height: 85vh;
          overflow-y: auto;
          position: relative;
          backdrop-filter: blur(20px);
        }
        .frame-detail-close {
          position: absolute;
          top: 12px;
          right: 15px;
          background: none;
          border: none;
          color: #fff;
          font-size: 1.5rem;
          cursor: pointer;
          opacity: 0.7;
          transition: opacity 0.3s;
        }
        .frame-detail-close:hover {
          opacity: 1;
        }
        .frame-detail-header {
          text-align: center;
          margin-bottom: 20px;
        }
        .frame-number {
          font-family: 'Inter', sans-serif;
          font-size: 0.8rem;
          color: #f0d78c;
          text-transform: uppercase;
          letter-spacing: 0.15rem;
        }
        .frame-detail-header h2 {
          font-family: 'DM Serif Display', serif;
          font-size: 1.6rem;
          color: #fff;
          margin: 8px 0 0 0;
        }
        .frame-detail-body {
          display: flex;
          gap: 20px;
          flex-wrap: wrap;
        }
        .frame-detail-image {
          flex: 1;
          min-width: 180px;
          max-width: 280px;
        }
        .frame-detail-image img {
          width: 100%;
          border-radius: 8px;
        }
        .frame-detail-text {
          flex: 1.5;
          min-width: 200px;
        }
        .frame-desc {
          font-family: 'DM Serif Display', serif;
          font-size: 1.1rem;
          color: #f0d78c;
          margin: 0 0 8px 0;
        }
        .frame-details {
          font-family: 'Inter', sans-serif;
          color: rgba(255,255,255,0.85);
          font-size: 0.85rem;
          line-height: 1.5;
          margin: 0 0 12px 0;
        }
        .frame-keywords {
          font-family: 'Inter', sans-serif;
          font-size: 0.75rem;
          color: rgba(240, 215, 140, 0.85);
          margin-bottom: 15px;
        }
        .frame-keywords strong {
          color: #f0d78c;
        }
        .frame-historical, .frame-modern {
          margin-bottom: 12px;
        }
        .frame-historical strong, .frame-modern strong {
          font-family: 'DM Serif Display', serif;
          color: #f0d78c;
          font-size: 0.85rem;
        }
        .frame-historical p, .frame-modern p {
          font-family: 'Inter', sans-serif;
          color: rgba(255,255,255,0.75);
          font-size: 0.8rem;
          line-height: 1.5;
          margin: 4px 0 0 0;
        }

        @keyframes fadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }

        @media (max-width: 768px) {
          .museum-banner h2 { font-size: 1.2rem; }
          .museum-banner p { font-size: 0.75rem; }
          .frame-detail-body { flex-direction: column; }
          .frame-detail-image { max-width: 100%; }
          .video-btn { top: 80px; right: 10px; padding: 8px 15px; font-size: 0.85rem; }
          .silk-road-btn { top: 130px; right: 10px; padding: 8px 15px; font-size: 0.85rem; }
          .frame-nav-btn { padding: 5px 10px; font-size: 0.7rem; }
          .video-content { padding: 15px 20px; }
          .video-content h3 { font-size: 1.1rem; }
          .video-player { max-height: 40vh; }
        }
      `}</style>
    </>
  );
};
