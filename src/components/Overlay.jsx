import { useEffect, useRef, useState } from 'react'
import { useProgress } from "@react-three/drei";
import { usePlay } from "../contexts/play";
import backgroundMusic from '../assets/HipHopLofi.mp3';
import { Link, useHistory } from 'react-router-dom';

export const Overlay = () => {
  const { progress } = useProgress();
  const { play, end, setPlay, hasScroll } = usePlay();
  const [isMusicPlaying, setIsMusicPlaying] = useState(false);
  const audioRef = useRef(new Audio(backgroundMusic));
  const history = useHistory();
  // ref 指向 outro 的 Link 元素，Enter 键时程序化触发 click
  const outroLinkRef = useRef(null);

  const playMusic = () => {
    const audio = audioRef.current;
    audio.play();
    setIsMusicPlaying(true);
  };

  const pauseMusic = () => {
    const audio = audioRef.current;
    audio.pause();
    setIsMusicPlaying(false);
  };

  // 预加载博物馆 GLB：旅程开始后在后台静默缓存，避免跳转时卡顿
  const preloadTriggered = useRef(false);
  useEffect(() => {
    if (play && !preloadTriggered.current) {
      preloadTriggered.current = true;
      const glbUrl = '/models/airplane/museumvr.glb';
      fetch(glbUrl, { cache: 'force-cache' })
        .then(() => console.log('[Preload] museumvr.glb cached'))
        .catch(() => {});
    }
  }, [play]);

  useEffect(() => {
    if (end) {
      setPlay(false);
    }
  }, [end, setPlay]);

  // Enter key: intro → start journey  /  outro → 触发 Link 跳转
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Enter') {
        if (progress === 100 && !play && !end) {
          e.preventDefault();
          setPlay(true);
        } else if (end) {
          e.preventDefault();
          // 直接触发 Link 元素的点击，React Router 内部处理导航
          if (outroLinkRef.current) {
            outroLinkRef.current.click();
          } else {
            // fallback: 万一 ref 没挂上
            history.push('/vrshow');
          }
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
    // 只依赖 end 和 play，不依赖 history 避免反复重绑定
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [end, play]);

  return (
    <div
      className={`overlay ${play  ? "overlay--disable" : ""}
    ${hasScroll ? "overlay--scrolled" : ""}`}
    >
      <div
        className={`loader ${progress === 100 ? "loader--disappear" : ""}`}
      />
      {progress === 100 && (
        <div className={`intro ${end || play ? "intro--disappear" : ''}`}>
          <h1 className="logo">
            Archaeology &amp; Technological Civilization
            <div className="spinner">
              <div className="spinner__image" />
            </div>
          </h1>
       
          {isMusicPlaying ? (
            <div class="loading-wave">
              <button className="PauseMusic" onClick={pauseMusic}>Pause</button>
              <div className="loading-bar"></div>
              <div className="loading-bar"></div>
              <div className="loading-bar"></div>
              <div className="loading-bar"></div>
            </div>
        ) : (
          <button className="music" onClick={playMusic}>Start Music</button>
        )}
          <p className="intro__scroll">Scroll to begin the journey</p>
          <button
            className="explore"
            onClick={() => {
              setPlay(true);
            }}
          >
            Enter Museum
          </button>
        </div>
      )}
      <div className={`outro ${end ? "outro--appear" : ""}`}>
        <p className="outro__text">Technology is becoming a new bridge between civilizations...</p>
      </div>
      <div className={`outro ${end ? "outro--appear" : ""}`}>
      <div class="card">
    <div class="align">
        <span class="red"></span>
        <span class="yellow"></span>
        <span class="green"></span>
    </div>
    <p className='Vrp'>Enter the Digital Museum Exhibition</p>
    <nav>
      <Link class='bn' to="/vrshow" ref={outroLinkRef}>Enter Museum</Link>
    </nav>
</div>
              
      </div>

    </div>
  );
};
