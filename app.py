<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
  <title>스타라이트 갤럭시 디펜더 - 네온 우주 슈팅 아케이드</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600;800;900&family=Noto+Sans+KR:wght@400;700;900&display=swap" rel="stylesheet" />
  <style>
    /* =========================================================================
       NEON CYBER ARCADE DESIGN SYSTEM
       ========================================================================= */
    :root {
      --bg-deep: #040711;
      --bg-panel: rgba(11, 18, 36, 0.88);
      --neon-cyan: #00f3ff;
      --neon-magenta: #ff2a85;
      --neon-amber: #ffbe0b;
      --neon-emerald: #00ff88;
      --text-main: #f0f6ff;
      --text-sub: #8ba3c7;
      --border-glow: rgba(0, 243, 255, 0.35);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
      touch-action: none;
    }

    html, body {
      width: 100%;
      height: 100%;
      background-color: var(--bg-deep);
      color: var(--text-main);
      font-family: 'Noto Sans KR', sans-serif;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
    }

    /* Main Game Container */
    .game-shell {
      position: relative;
      width: 100%;
      max-width: 960px;
      height: 100%;
      max-height: 820px;
      display: flex;
      flex-direction: column;
      padding: 10px;
      gap: 10px;
    }

    /* Top Telemetry HUD Bar */
    .hud-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      background: var(--bg-panel);
      border: 1px solid var(--border-glow);
      border-radius: 14px;
      padding: 8px 14px;
      backdrop-filter: blur(10px);
      box-shadow: 0 0 20px rgba(0, 243, 255, 0.12);
      z-index: 10;
    }

    .hud-group {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .stat-box {
      display: flex;
      flex-direction: column;
    }

    .stat-label {
      font-size: 10px;
      font-weight: 700;
      color: var(--text-sub);
      letter-spacing: 0.06em;
    }

    .stat-value {
      font-family: 'Orbitron', sans-serif;
      font-size: 16px;
      font-weight: 800;
      color: var(--neon-cyan);
      text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
    }

    .stat-value.amber {
      color: var(--neon-amber);
      text-shadow: 0 0 10px rgba(255, 190, 11, 0.5);
    }

    .stat-value.magenta {
      color: var(--neon-magenta);
      text-shadow: 0 0 10px rgba(255, 42, 133, 0.5);
    }

    /* HP & Overdrive Bars */
    .bar-wrap {
      display: flex;
      flex-direction: column;
      gap: 3px;
      min-width: 110px;
    }

    .bar-track {
      width: 100%;
      height: 8px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 999px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }

    .bar-fill-hp {
      height: 100%;
      width: 100%;
      background: linear-gradient(90deg, #ff2a85, #00ff88);
      border-radius: 999px;
      transition: width 0.15s ease-out;
    }

    .bar-fill-ult {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #00f3ff, #ffbe0b);
      border-radius: 999px;
      transition: width 0.12s ease-out;
    }

    /* Canvas Stage */
    .canvas-stage {
      position: relative;
      flex: 1;
      width: 100%;
      min-height: 0;
      border-radius: 16px;
      overflow: hidden;
      border: 1.5px solid var(--border-glow);
      box-shadow: 0 12px 40px rgba(0, 0, 0, 0.75), inset 0 0 30px rgba(0, 243, 255, 0.08);
      background: radial-gradient(circle at 50% 30%, #0b152c 0%, #03060e 100%);
    }

    canvas {
      display: block;
      width: 100%;
      height: 100%;
      cursor: crosshair;
    }

    /* Bottom External Control Strip */
    .control-bar {
      display: flex;
      align-items: center;
      justify-content: center;
      flex-wrap: wrap;
      gap: 10px;
      padding: 4px 8px;
      z-index: 10;
    }

    .arcade-btn {
      font-family: 'Noto Sans KR', sans-serif;
      font-weight: 800;
      font-size: 13px;
      color: var(--text-main);
      background: linear-gradient(180deg, rgba(22, 36, 68, 0.95) 0%, rgba(10, 17, 36, 0.98) 100%);
      border: 1.5px solid rgba(0, 243, 255, 0.45);
      border-radius: 12px;
      padding: 10px 16px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.15);
      transition: transform 0.12s ease, box-shadow 0.15s ease, border-color 0.15s ease;
    }

    .arcade-btn:hover {
      transform: translateY(-2px);
      border-color: var(--neon-cyan);
      box-shadow: 0 6px 20px rgba(0, 243, 255, 0.35), inset 0 1px 0 rgba(255, 255, 255, 0.25);
    }

    .arcade-btn:active {
      transform: translateY(1px) scale(0.97);
    }

    .arcade-btn.nova-ready {
      background: linear-gradient(135deg, #ff2a85 0%, #ffbe0b 100%);
      color: #050811;
      border-color: #ffffff;
      animation: pulseNova 1s infinite alternate;
    }

    @keyframes pulseNova {
      from { box-shadow: 0 0 12px rgba(255, 42, 133, 0.7); }
      to   { box-shadow: 0 0 26px rgba(255, 190, 11, 0.95); }
    }

    /* Overlay Screens (Start / Game Over / Pause) */
    .overlay-modal {
      position: absolute;
      inset: 0;
      background: rgba(4, 7, 17, 0.82);
      backdrop-filter: blur(8px);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding: 24px;
      z-index: 20;
      transition: opacity 0.25s ease;
    }

    .overlay-modal.hidden {
      opacity: 0;
      pointer-events: none;
    }

    .title-badge {
      font-family: 'Orbitron', sans-serif;
      font-size: 11px;
      font-weight: 800;
      letter-spacing: 0.2em;
      color: var(--neon-amber);
      background: rgba(255, 190, 11, 0.14);
      border: 1px solid rgba(255, 190, 11, 0.45);
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }

    .main-title {
      font-family: 'Orbitron', 'Noto Sans KR', sans-serif;
      font-size: clamp(26px, 5vw, 44px);
      font-weight: 900;
      line-height: 1.15;
      background: linear-gradient(135deg, #ffffff 0%, #00f3ff 55%, #ff2a85 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      filter: drop-shadow(0 0 18px rgba(0, 243, 255, 0.35));
      margin-bottom: 10px;
    }

    .sub-desc {
      max-width: 460px;
      font-size: 14px;
      line-height: 1.6;
      color: var(--text-sub);
      margin-bottom: 22px;
    }

    .guide-pills {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 8px;
      margin-bottom: 24px;
      max-width: 520px;
    }

    .pill {
      font-size: 12px;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.14);
      border-radius: 10px;
      padding: 6px 11px;
      color: #dbeafe;
    }

    .start-cta {
      font-family: 'Noto Sans KR', sans-serif;
      font-size: 17px;
      font-weight: 900;
      color: #030712;
      background: linear-gradient(135deg, #00f3ff 0%, #00ff88 100%);
      border: none;
      border-radius: 14px;
      padding: 14px 34px;
      cursor: pointer;
      box-shadow: 0 0 28px rgba(0, 243, 255, 0.55);
      transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .start-cta:hover {
      transform: scale(1.05);
      box-shadow: 0 0 38px rgba(0, 255, 136, 0.8);
    }

    .start-cta:active {
      transform: scale(0.97);
    }

    .result-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      width: 100%;
      max-width: 440px;
      margin-bottom: 22px;
    }

    .result-card {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(0, 243, 255, 0.25);
      border-radius: 12px;
      padding: 10px 8px;
    }

    .result-card .val {
      font-family: 'Orbitron', sans-serif;
      font-size: 18px;
      font-weight: 800;
      color: var(--neon-cyan);
      margin-top: 4px;
    }
  </style>
</head>
<body>

  <div class="game-shell">
    <!-- Top HUD Telemetry -->
    <header class="hud-bar">
      <div class="hud-group">
        <div class="stat-box">
          <span class="stat-label">SCORE</span>
          <span class="stat-value" id="hudScore">0</span>
        </div>
        <div class="stat-box">
          <span class="stat-label">WAVE</span>
          <span class="stat-value amber" id="hudWave">1</span>
        </div>
        <div class="stat-box">
          <span class="stat-label">COMBO</span>
          <span class="stat-value magenta" id="hudCombo">x1</span>
        </div>
      </div>

      <div class="hud-group">
        <div class="bar-wrap">
          <div style="display:flex; justify-content:space-between;">
            <span class="stat-label">SHIELD HP</span>
            <span class="stat-label" id="hudHpText">100%</span>
          </div>
          <div class="bar-track">
            <div class="bar-fill-hp" id="hudHpBar"></div>
          </div>
        </div>

        <div class="bar-wrap">
          <div style="display:flex; justify-content:space-between;">
            <span class="stat-label">NOVA OVERDRIVE</span>
            <span class="stat-label" id="hudUltText">0%</span>
          </div>
          <div class="bar-track">
            <div class="bar-fill-ult" id="hudUltBar"></div>
          </div>
        </div>
      </div>
    </header>

    <!-- Main Game Canvas Stage -->
    <main class="canvas-stage" id="canvasStage">
      <canvas id="gameCanvas"></canvas>

      <!-- Start Screen Overlay -->
      <div class="overlay-modal" id="startOverlay">
        <div class="title-badge">NEON CYBER SHOOTER</div>
        <h1 class="main-title">STARLIGHT<br>DEFENDER</h1>
        <p class="sub-desc">
          은하계 외곽 방어선을 돌파하려는 네온 함대와 거대 드레드노트 보스를 격퇴하세요! 파워업 코어를 수집해 레이저를 진화시키고 노바 폭탄으로 전장을 휩쓸어보세요.
        </p>
        <div class="guide-pills">
          <span class="pill">🕹️ 이동: 방향키 / WASD / 마우스·터치 드래그</span>
          <span class="pill">⚡ 자동 사격 지원</span>
          <span class="pill">💥 필살기: Space / Shift / 노바 버튼</span>
        </div>
        <button class="start-cta" id="btnStartGame" type="button">🚀 출격 시작 (PLAY)</button>
      </div>

      <!-- Game Over Overlay -->
      <div class="overlay-modal hidden" id="gameOverOverlay">
        <div class="title-badge" style="color:#ff2a85; border-color:rgba(255,42,133,0.5);">MISSION TERMINATED</div>
        <h2 class="main-title">함선 대파</h2>
        <p class="sub-desc" id="gameOverReason">네온 함대의 집중 포화에 쉴드가 붕괴되었습니다.</p>
        <div class="result-grid">
          <div class="result-card">
            <div class="stat-label">최종 점수</div>
            <div class="val" id="finalScore">0</div>
          </div>
          <div class="result-card">
            <div class="stat-label">도달 웨이브</div>
            <div class="val" id="finalWave" style="color:#ffbe0b;">1</div>
          </div>
          <div class="result-card">
            <div class="stat-label">최고 콤보</div>
            <div class="val" id="finalCombo" style="color:#ff2a85;">x1</div>
          </div>
        </div>
        <button class="start-cta" id="btnRestartGame" type="button">🔄 다시 출격하기 (RETRY)</button>
      </div>
    </main>

    <!-- External Control Buttons Bar -->
    <footer class="control-bar">
      <button class="arcade-btn" id="btnNova" type="button">💥 노바 폭탄 (SPACE)</button>
      <button class="arcade-btn" id="btnPause" type="button">⏸️ 일시정지</button>
      <button class="arcade-btn" id="btnSound" type="button">🔊 사운드 ON</button>
    </footer>
  </div>

  <script>
    (() => {
      'use strict';

      /* =======================================================================
         1. WEB AUDIO API RETRO SYNTHESIZER (NO EXTERNAL AUDIO URLS)
         ======================================================================= */
      class ArcadeSynth {
        constructor() {
          this.ctx = null;
          this.muted = false;
        }

        unlock() {
          if (!this.ctx) {
            const AudioCtx = window.AudioContext || window.webkitAudioContext;
            if (AudioCtx) this.ctx = new AudioCtx();
          }
          if (this.ctx && this.ctx.state === 'suspended') {
            this.ctx.resume().catch(() => {});
          }
        }

        toggleMute() {
          this.muted = !this.muted;
          return this.muted;
        }

        playLaser(level = 1) {
          if (this.muted || !this.ctx) return;
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = level >= 3 ? 'sawtooth' : 'triangle';
          const baseFreq = 720 + level * 90;
          osc.frequency.setValueAtTime(baseFreq, now);
          osc.frequency.exponentialRampToValueAtTime(190, now + 0.08);
          gain.gain.setValueAtTime(0.055, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.085);
        }

        playExplosion(isBig = false) {
          if (this.muted || !this.ctx) return;
          const now = this.ctx.currentTime;
          const duration = isBig ? 0.55 : 0.22;
          const bufferSize = Math.floor(this.ctx.sampleRate * duration);
          const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
          const data = buffer.getChannelData(0);
          for (let i = 0; i < bufferSize; i++) {
            data[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / bufferSize, 1.8);
          }

          const noise = this.ctx.createBufferSource();
          noise.buffer = buffer;

          const filter = this.ctx.createBiquadFilter();
          filter.type = 'lowpass';
          filter.frequency.setValueAtTime(isBig ? 420 : 750, now);
          filter.frequency.exponentialRampToValueAtTime(65, now + duration);

          const gain = this.ctx.createGain();
          gain.gain.setValueAtTime(isBig ? 0.22 : 0.11, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + duration);

          noise.connect(filter);
          filter.connect(gain);
          gain.connect(this.ctx.destination);
          noise.start(now);
        }

        playPowerup() {
          if (this.muted || !this.ctx) return;
          const now = this.ctx.currentTime;
          [523.25, 659.25, 783.99, 1046.5].forEach((freq, idx) => {
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(freq, now + idx * 0.05);
            gain.gain.setValueAtTime(0.08, now + idx * 0.05);
            gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.05 + 0.16);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + idx * 0.05);
            osc.stop(now + idx * 0.05 + 0.17);
          });
        }

        playHit() {
          if (this.muted || !this.ctx) return;
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sawtooth';
          osc.frequency.setValueAtTime(160, now);
          osc.frequency.exponentialRampToValueAtTime(55, now + 0.18);
          gain.gain.setValueAtTime(0.14, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.18);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.19);
        }

        playNova() {
          if (this.muted || !this.ctx) return;
          this.playExplosion(true);
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(140, now);
          osc.frequency.exponentialRampToValueAtTime(880, now + 0.35);
          gain.gain.setValueAtTime(0.16, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.46);
        }
      }

      const synth = new ArcadeSynth();

      /* =======================================================================
         2. RESPONSIVE CANVAS SETUP & GAME STATE
         ======================================================================= */
      const canvas = document.getElementById('gameCanvas');
      const ctx = canvas.getContext('2d');
      const stageEl = document.getElementById('canvasStage');

      let W = 800;
      let H = 600;

      function resizeCanvas() {
        const rect = stageEl.getBoundingClientRect();
        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        W = Math.max(320, rect.width);
        H = Math.max(360, rect.height);
        canvas.width = Math.floor(W * dpr);
        canvas.height = Math.floor(H * dpr);
        ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

        if (game.player) {
          game.player.x = Math.max(24, Math.min(W - 24, game.player.x));
          game.player.y = Math.max(40, Math.min(H - 28, game.player.y));
        }
      }

      window.addEventListener('resize', resizeCanvas);

      const game = {
        mode: 'menu', // 'menu' | 'playing' | 'paused' | 'gameover'
        score: 0,
        highScore: 0,
        wave: 1,
        combo: 1,
        maxCombo: 1,
        comboTimer: 0,
        novaCharge: 0, // 0..100
        novaWaveRadius: 0,
        novaActive: false,
        screenShake: 0,
        waveBannerTimer: 0,
        waveBannerText: '',
        spawnTimer: 0,
        waveKills: 0,
        waveQuota: 12,
        bossActive: false,
        player: null,
        bullets: [],
        enemyBullets: [],
        enemies: [],
        particles: [],
        powerups: [],
        floatingTexts: [],
        stars: []
      };

      function initStars() {
        game.stars = [];
        for (let i = 0; i < 85; i++) {
          game.stars.push({
            x: Math.random() * W,
            y: Math.random() * H,
            size: Math.random() * 2 + 0.6,
            speed: Math.random() * 95 + 25,
            alpha: Math.random() * 0.7 + 0.2
          });
        }
      }

      function resetGame() {
        game.mode = 'playing';
        game.score = 0;
        game.wave = 1;
        game.combo = 1;
        game.maxCombo = 1;
        game.comboTimer = 0;
        game.novaCharge = 40;
        game.novaActive = false;
        game.novaWaveRadius = 0;
        game.screenShake = 0;
        game.waveKills = 0;
        game.waveQuota = 12;
        game.bossActive = false;
        game.spawnTimer = 0.4;

        game.player = {
          x: W / 2,
          y: H - 70,
          r: 18,
          hp: 100,
          maxHp: 100,
          weaponLevel: 1,
          fireCooldown: 0,
          invulnTimer: 1.2,
          shieldTimer: 0
        };

        game.bullets = [];
        game.enemyBullets = [];
        game.enemies = [];
        game.particles = [];
        game.powerups = [];
        game.floatingTexts = [];

        triggerWaveBanner('WAVE 1 — 방어선 교전 개시');
        updateHud();
      }

      function triggerWaveBanner(text) {
        game.waveBannerText = text;
        game.waveBannerTimer = 2.4;
      }

      /* =======================================================================
         3. INPUT HANDLERS (KEYBOARD, MOUSE, TOUCH)
         ======================================================================= */
      const keys = {};
      const pointer = { active: false, x: 0, y: 0 };

      window.addEventListener('keydown', (e) => {
        keys[e.code] = true;
        if (['ArrowUp', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'Space'].includes(e.code)) {
          e.preventDefault();
        }
        if ((e.code === 'Space' || e.code === 'ShiftLeft' || e.code === 'ShiftRight') && game.mode === 'playing') {
          activateNovaBomb();
        }
        if (e.code === 'KeyP' || e.code === 'Escape') {
          togglePause();
        }
      });

      window.addEventListener('keyup', (e) => {
        keys[e.code] = false;
      });

      function updatePointerPos(clientX, clientY) {
        const rect = canvas.getBoundingClientRect();
        pointer.x = clientX - rect.left;
        pointer.y = clientY - rect.top - 22; // Slight offset so finger doesn't cover ship
      }

      canvas.addEventListener('mousedown', (e) => {
        if (game.mode !== 'playing') return;
        pointer.active = true;
        updatePointerPos(e.clientX, e.clientY);
      });

      window.addEventListener('mousemove', (e) => {
        if (!pointer.active || game.mode !== 'playing') return;
        updatePointerPos(e.clientX, e.clientY);
      });

      window.addEventListener('mouseup', () => {
        pointer.active = false;
      });

      canvas.addEventListener('touchstart', (e) => {
        if (game.mode !== 'playing') return;
        e.preventDefault();
        if (e.touches.length > 0) {
          pointer.active = true;
          updatePointerPos(e.touches[0].clientX, e.touches[0].clientY);
        }
      }, { passive: false });

      canvas.addEventListener('touchmove', (e) => {
        if (game.mode !== 'playing') return;
        e.preventDefault();
        if (e.touches.length > 0) {
          updatePointerPos(e.touches[0].clientX, e.touches[0].clientY);
        }
      }, { passive: false });

      canvas.addEventListener('touchend', () => {
        pointer.active = false;
      });

      /* =======================================================================
         4. COMBAT MECHANICS, ENEMY SPAWNING & POWERUPS
         ======================================================================= */
      function spawnPlayerBullets() {
        const p = game.player;
        const lv = p.weaponLevel;
        synth.playLaser(lv);

        if (lv === 1) {
          game.bullets.push({ x: p.x, y: p.y - 20, vx: 0, vy: -680, dmg: 14, color: '#00f3ff', r: 4 });
        } else if (lv === 2) {
          game.bullets.push({ x: p.x - 10, y: p.y - 16, vx: 0, vy: -700, dmg: 13, color: '#00f3ff', r: 4 });
          game.bullets.push({ x: p.x + 10, y: p.y - 16, vx: 0, vy: -700, dmg: 13, color: '#00f3ff', r: 4 });
        } else if (lv === 3) {
          game.bullets.push({ x: p.x, y: p.y - 22, vx: 0, vy: -740, dmg: 16, color: '#00ff88', r: 4.5 });
          game.bullets.push({ x: p.x - 13, y: p.y - 14, vx: -75, vy: -710, dmg: 12, color: '#00f3ff', r: 4 });
          game.bullets.push({ x: p.x + 13, y: p.y - 14, vx: 75, vy: -710, dmg: 12, color: '#00f3ff', r: 4 });
        } else {
          // Max Overclock Quad + Wing Plasma
          game.bullets.push({ x: p.x - 7, y: p.y - 22, vx: 0, vy: -780, dmg: 16, color: '#ffbe0b', r: 4.5 });
          game.bullets.push({ x: p.x + 7, y: p.y - 22, vx: 0, vy: -780, dmg: 16, color: '#ffbe0b', r: 4.5 });
          game.bullets.push({ x: p.x - 18, y: p.y - 12, vx: -115, vy: -740, dmg: 13, color: '#00ff88', r: 4 });
          game.bullets.push({ x: p.x + 18, y: p.y - 12, vx: 115, vy: -740, dmg: 13, color: '#00ff88', r: 4 });
        }
      }

      function spawnEnemy() {
        const margin = 44;
        const x = margin + Math.random() * (W - margin * 2);
        const waveScale = 1 + (game.wave - 1) * 0.16;
        const roll = Math.random();

        if (roll < 0.5) {
          // Scout Drone (Fast, zig-zag)
          game.enemies.push({
            type: 'scout',
            x,
            y: -28,
            r: 16,
            hp: Math.round(24 * waveScale),
            maxHp: Math.round(24 * waveScale),
            vy: 145 + game.wave * 10,
            phase: Math.random() * Math.PI * 2,
            shootTimer: 1.5 + Math.random() * 1.4,
            scoreVal: 120,
            color: '#ff2a85'
          });
        } else if (roll < 0.82) {
          // Interceptor (Aimed burst shooter)
          game.enemies.push({
            type: 'interceptor',
            x,
            y: -32,
            r: 20,
            hp: Math.round(46 * waveScale),
            maxHp: Math.round(46 * waveScale),
            vy: 95 + game.wave * 6,
            phase: Math.random() * Math.PI * 2,
            shootTimer: 1.1 + Math.random() * 0.9,
            scoreVal: 240,
            color: '#ffbe0b'
          });
        } else {
          // Heavy Cruiser (Armored tank)
          game.enemies.push({
            type: 'cruiser',
            x,
            y: -40,
            r: 28,
            hp: Math.round(95 * waveScale),
            maxHp: Math.round(95 * waveScale),
            vy: 58 + game.wave * 4,
            phase: 0,
            shootTimer: 1.4,
            scoreVal: 450,
            color: '#a855f7'
          });
        }
      }

      function spawnBoss() {
        game.bossActive = true;
        const bossHp = Math.round(950 + (game.wave - 1) * 520);
        triggerWaveBanner(`⚠️ WARNING: DREADNOUGHT BOSS 출현!`);
        synth.playNova();

        game.enemies.push({
          type: 'boss',
          x: W / 2,
          y: -85,
          targetY: 105,
          r: 56,
          hp: bossHp,
          maxHp: bossHp,
          vy: 65,
          phase: 0,
          shootTimer: 1.0,
          patternIdx: 0,
          scoreVal: 3500,
          color: '#ff2a85'
        });
      }

      function activateNovaBomb() {
        if (game.mode !== 'playing' || game.novaCharge < 100) return;
        game.novaCharge = 0;
        game.novaActive = true;
        game.novaWaveRadius = 10;
        game.screenShake = 16;
        synth.playNova();

        // Clear all enemy projectiles
        game.enemyBullets = [];
        addFloatingText(game.player.x, game.player.y - 35, 'NOVA OVERDRIVE!!', '#ffbe0b');

        // Deal massive area damage to all enemies
        for (let i = game.enemies.length - 1; i >= 0; i--) {
          const e = game.enemies[i];
          damageEnemy(e, i, 320);
        }
        updateHud();
      }

      function spawnParticles(x, y, color, count = 14, speedMult = 1) {
        for (let i = 0; i < count; i++) {
          const angle = Math.random() * Math.PI * 2;
          const speed = (Math.random() * 180 + 45) * speedMult;
          game.particles.push({
            x,
            y,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            life: 0.35 + Math.random() * 0.35,
            maxLife: 0.7,
            size: Math.random() * 3.5 + 1.5,
            color
          });
        }
      }

      function addFloatingText(x, y, text, color = '#00f3ff') {
        game.floatingTexts.push({
          x,
          y,
          text,
          color,
          life: 0.95
        });
      }

      function maybeDropPowerup(x, y) {
        if (Math.random() > 0.24) return;
        const types = [
          { kind: 'weapon', label: 'P', color: '#00f3ff' },
          { kind: 'heal',   label: '+', color: '#00ff88' },
          { kind: 'nova',   label: 'N', color: '#ffbe0b' }
        ];
        const chosen = types[Math.floor(Math.random() * types.length)];
        game.powerups.push({
          x,
          y,
          vy: 110,
          r: 14,
          kind: chosen.kind,
          label: chosen.label,
          color: chosen.color,
          pulse: 0
        });
      }

      function damageEnemy(enemy, index, dmg) {
        enemy.hp -= dmg;
        if (enemy.hp <= 0) {
          const isBoss = enemy.type === 'boss';
          synth.playExplosion(isBoss || enemy.type === 'cruiser');
          spawnParticles(enemy.x, enemy.y, enemy.color, isBoss ? 48 : 16, isBoss ? 1.5 : 1);
          game.screenShake = Math.max(game.screenShake, isBoss ? 18 : 5);

          // Score & Combo calculation
          const gained = enemy.scoreVal * game.combo;
          game.score += gained;
          if (game.score > game.highScore) game.highScore = game.score;

          game.combo = Math.min(25, game.combo + 1);
          if (game.combo > game.maxCombo) game.maxCombo = game.combo;
          game.comboTimer = 3.2;

          game.novaCharge = Math.min(100, game.novaCharge + (isBoss ? 50 : 9));
          addFloatingText(enemy.x, enemy.y, `+${gained}`, '#00ff88');

          if (isBoss) {
            game.bossActive = false;
            game.wave += 1;
            game.waveKills = 0;
            game.waveQuota = 12 + game.wave * 3;
            triggerWaveBanner(`WAVE ${game.wave} 진입! 적 함대 증원`);
            // Guaranteed drops from boss
            game.powerups.push({ x: enemy.x - 24, y: enemy.y, vy: 95, r: 14, kind: 'weapon', label: 'P', color: '#00f3ff', pulse: 0 });
            game.powerups.push({ x: enemy.x + 24, y: enemy.y, vy: 95, r: 14, kind: 'heal', label: '+', color: '#00ff88', pulse: 0 });
          } else {
            maybeDropPowerup(enemy.x, enemy.y);
            game.waveKills += 1;
            if (!game.bossActive && game.waveKills >= game.waveQuota) {
              spawnBoss();
            }
          }

          game.enemies.splice(index, 1);
          updateHud();
        }
      }

      function damagePlayer(amount) {
        const p = game.player;
        if (p.invulnTimer > 0) return;

        p.hp = Math.max(0, p.hp - amount);
        p.invulnTimer = 0.85;
        game.combo = 1;
        game.screenShake = 12;
        synth.playHit();
        spawnParticles(p.x, p.y, '#ff2a85', 18, 1.1);
        addFloatingText(p.x, p.y - 24, `-${amount} SHIELD`, '#ff2a85');
        updateHud();

        if (p.hp <= 0) {
          endGame();
        }
      }

      function endGame() {
        game.mode = 'gameover';
        synth.playExplosion(true);
        document.getElementById('finalScore').textContent = game.score.toLocaleString();
        document.getElementById('finalWave').textContent = game.wave;
        document.getElementById('finalCombo').textContent = `x${game.maxCombo}`;
        document.getElementById('gameOverOverlay').classList.remove('hidden');
      }

      /* =======================================================================
         5. UPDATE & SIMULATION LOOP
         ======================================================================= */
      function update(dt) {
        // Animate starfield even on menu
        for (const s of game.stars) {
          s.y += s.speed * dt;
          if (s.y > H) {
            s.y = -4;
            s.x = Math.random() * W;
          }
        }

        if (game.mode !== 'playing') return;

        const p = game.player;
        if (p.invulnTimer > 0) p.invulnTimer = Math.max(0, p.invulnTimer - dt);
        if (game.screenShake > 0) game.screenShake = Math.max(0, game.screenShake - dt * 32);
        if (game.waveBannerTimer > 0) game.waveBannerTimer = Math.max(0, game.waveBannerTimer - dt);

        // Combo decay
        if (game.combo > 1) {
          game.comboTimer -= dt;
          if (game.comboTimer <= 0) {
            game.combo = 1;
            updateHud();
          }
        }

        // Nova shockwave animation
        if (game.novaActive) {
          game.novaWaveRadius += dt * 950;
          if (game.novaWaveRadius > Math.max(W, H) * 1.2) {
            game.novaActive = false;
          }
        }

        // Player Movement (Keyboard + Smooth Pointer Follow)
        const moveSpeed = 390;
        let dx = 0;
        let dy = 0;
        if (keys['ArrowLeft'] || keys['KeyA']) dx -= 1;
        if (keys['ArrowRight'] || keys['KeyD']) dx += 1;
        if (keys['ArrowUp'] || keys['KeyW']) dy -= 1;
        if (keys['ArrowDown'] || keys['KeyS']) dy += 1;

        if (dx !== 0 || dy !== 0) {
          const len = Math.hypot(dx, dy);
          p.x += (dx / len) * moveSpeed * dt;
          p.y += (dy / len) * moveSpeed * dt;
        } else if (pointer.active) {
          const lerp = Math.min(1, dt * 16);
          p.x += (pointer.x - p.x) * lerp;
          p.y += (pointer.y - p.y) * lerp;
        }

        p.x = Math.max(24, Math.min(W - 24, p.x));
        p.y = Math.max(40, Math.min(H - 28, p.y));

        // Auto-fire player weapons
        p.fireCooldown -= dt;
        if (p.fireCooldown <= 0) {
          spawnPlayerBullets();
          p.fireCooldown = Math.max(0.11, 0.19 - p.weaponLevel * 0.018);
        }

        // Spawn Enemies
        if (!game.bossActive) {
          game.spawnTimer -= dt;
          if (game.spawnTimer <= 0) {
            spawnEnemy();
            game.spawnTimer = Math.max(0.38, 1.15 - game.wave * 0.08);
          }
        }

        // Update Player Bullets
        for (let i = game.bullets.length - 1; i >= 0; i--) {
          const b = game.bullets[i];
          b.x += b.vx * dt;
          b.y += b.vy * dt;
          if (b.y < -20 || b.x < -20 || b.x > W + 20) {
            game.bullets.splice(i, 1);
            continue;
          }

          // Bullet vs Enemy collision
          for (let j = game.enemies.length - 1; j >= 0; j--) {
            const e = game.enemies[j];
            if (Math.hypot(b.x - e.x, b.y - e.y) < e.r + b.r) {
              spawnParticles(b.x, b.y, b.color, 4, 0.5);
              game.bullets.splice(i, 1);
              damageEnemy(e, j, b.dmg);
              break;
            }
          }
        }

        // Update Enemies
        for (let i = game.enemies.length - 1; i >= 0; i--) {
          const e = game.enemies[i];
          e.phase += dt * 3.2;

          if (e.type === 'scout') {
            e.y += e.vy * dt;
            e.x += Math.sin(e.phase) * 120 * dt;
          } else if (e.type === 'interceptor') {
            e.y += e.vy * dt;
            e.x += Math.cos(e.phase * 0.7) * 65 * dt;
          } else if (e.type === 'cruiser') {
            e.y += e.vy * dt;
          } else if (e.type === 'boss') {
            if (e.y < e.targetY) {
              e.y += e.vy * dt;
            } else {
              e.x = W / 2 + Math.sin(e.phase * 0.55) * (W * 0.32);
            }
          }

          e.x = Math.max(e.r + 10, Math.min(W - e.r - 10, e.x));

          // Enemy shooting logic
          e.shootTimer -= dt;
          if (e.shootTimer <= 0 && e.y > 20 && e.y < H - 120) {
            const ang = Math.atan2(p.y - e.y, p.x - e.x);
            if (e.type === 'scout') {
              game.enemyBullets.push({ x: e.x, y: e.y + 14, vx: 0, vy: 270, r: 5, color: '#ff2a85' });
              e.shootTimer = 2.2;
            } else if (e.type === 'interceptor') {
              const spd = 300;
              game.enemyBullets.push({ x: e.x, y: e.y + 16, vx: Math.cos(ang) * spd, vy: Math.sin(ang) * spd, r: 5.5, color: '#ffbe0b' });
              e.shootTimer = 1.7;
            } else if (e.type === 'cruiser') {
              [-0.25, 0, 0.25].forEach(offset => {
                const a = ang + offset;
                game.enemyBullets.push({ x: e.x, y: e.y + 22, vx: Math.cos(a) * 260, vy: Math.sin(a) * 260, r: 6, color: '#c084fc' });
              });
              e.shootTimer = 2.1;
            } else if (e.type === 'boss') {
              e.patternIdx = (e.patternIdx + 1) % 3;
              if (e.patternIdx === 0) {
                // Radial fan burst
                for (let k = -3; k <= 3; k++) {
                  const a = Math.PI / 2 + k * 0.22;
                  game.enemyBullets.push({ x: e.x, y: e.y + 42, vx: Math.cos(a) * 285, vy: Math.sin(a) * 285, r: 6.5, color: '#ff2a85' });
                }
              } else if (e.patternIdx === 1) {
                // Twin aimed plasma
                [-26, 26].forEach(ox => {
                  const a = Math.atan2(p.y - (e.y + 30), p.x - (e.x + ox));
                  game.enemyBullets.push({ x: e.x + ox, y: e.y + 30, vx: Math.cos(a) * 340, vy: Math.sin(a) * 340, r: 6, color: '#ffbe0b' });
                });
              } else {
                // Ring pulse
                for (let k = 0; k < 10; k++) {
                  const a = (Math.PI * 2 * k) / 10 + e.phase;
                  game.enemyBullets.push({ x: e.x, y: e.y + 20, vx: Math.cos(a) * 220, vy: Math.sin(a) * 220, r: 5.5, color: '#00f3ff' });
                }
              }
              e.shootTimer = Math.max(0.75, 1.25 - game.wave * 0.06);
            }
          }

          // Enemy vs Player body collision
          if (Math.hypot(e.x - p.x, e.y - p.y) < e.r + p.r - 4) {
            damagePlayer(e.type === 'boss' ? 35 : 22);
            if (e.type !== 'boss') {
              spawnParticles(e.x, e.y, e.color, 14, 1);
              game.enemies.splice(i, 1);
              continue;
            }
          }

          // Out of bottom bounds
          if (e.y > H + 60) {
            game.enemies.splice(i, 1);
          }
        }

        // Update Enemy Bullets
        for (let i = game.enemyBullets.length - 1; i >= 0; i--) {
          const eb = game.enemyBullets[i];
          eb.x += eb.vx * dt;
          eb.y += eb.vy * dt;
          if (eb.y > H + 20 || eb.y < -30 || eb.x < -30 || eb.x > W + 30) {
            game.enemyBullets.splice(i, 1);
            continue;
          }

          if (Math.hypot(eb.x - p.x, eb.y - p.y) < eb.r + p.r - 5) {
            game.enemyBullets.splice(i, 1);
            damagePlayer(15);
          }
        }

        // Update Powerups
        for (let i = game.powerups.length - 1; i >= 0; i--) {
          const pw = game.powerups[i];
          pw.y += pw.vy * dt;
          pw.pulse += dt * 6;

          if (Math.hypot(pw.x - p.x, pw.y - p.y) < pw.r + p.r + 6) {
            synth.playPowerup();
            if (pw.kind === 'weapon') {
              if (p.weaponLevel < 4) {
                p.weaponLevel += 1;
                addFloatingText(p.x, p.y - 28, `WEAPON LV.${p.weaponLevel}!`, '#00f3ff');
              } else {
                game.score += 1000;
                addFloatingText(p.x, p.y - 28, 'MAX POWER +1000!', '#00f3ff');
              }
            } else if (pw.kind === 'heal') {
              p.hp = Math.min(p.maxHp, p.hp + 30);
              addFloatingText(p.x, p.y - 28, 'SHIELD +30%', '#00ff88');
            } else if (pw.kind === 'nova') {
              game.novaCharge = Math.min(100, game.novaCharge + 50);
              addFloatingText(p.x, p.y - 28, 'NOVA +50%', '#ffbe0b');
            }
            updateHud();
            game.powerups.splice(i, 1);
            continue;
          }

          if (pw.y > H + 30) {
            game.powerups.splice(i, 1);
          }
        }

        // Update Particles
        for (let i = game.particles.length - 1; i >= 0; i--) {
          const pt = game.particles[i];
          pt.x += pt.vx * dt;
          pt.y += pt.vy * dt;
          pt.vx *= 0.96;
          pt.vy *= 0.96;
          pt.life -= dt;
          if (pt.life <= 0) game.particles.splice(i, 1);
        }

        // Update Floating Texts
        for (let i = game.floatingTexts.length - 1; i >= 0; i--) {
          const ft = game.floatingTexts[i];
          ft.y -= 42 * dt;
          ft.life -= dt;
          if (ft.life <= 0) game.floatingTexts.splice(i, 1);
        }
      }

      /* =======================================================================
         6. NEON VECTOR & PARTICLE RENDERER
         ======================================================================= */
      function draw() {
        ctx.save();
        if (game.screenShake > 0) {
          const sx = (Math.random() - 0.5) * game.screenShake;
          const sy = (Math.random() - 0.5) * game.screenShake;
          ctx.translate(sx, sy);
        }

        ctx.clearRect(-20, -20, W + 40, H + 40);

        // Starfield
        for (const s of game.stars) {
          ctx.fillStyle = `rgba(210, 235, 255, ${s.alpha})`;
          ctx.beginPath();
          ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
          ctx.fill();
        }

        // Nova Shockwave Ring
        if (game.novaActive && game.player) {
          ctx.save();
          ctx.strokeStyle = 'rgba(255, 190, 11, 0.85)';
          ctx.lineWidth = 8;
          ctx.shadowColor = '#ff2a85';
          ctx.shadowBlur = 24;
          ctx.beginPath();
          ctx.arc(game.player.x, game.player.y, game.novaWaveRadius, 0, Math.PI * 2);
          ctx.stroke();
          ctx.restore();
        }

        // Powerups
        for (const pw of game.powerups) {
          ctx.save();
          const scale = 1 + Math.sin(pw.pulse) * 0.12;
          ctx.translate(pw.x, pw.y);
          ctx.scale(scale, scale);
          ctx.shadowColor = pw.color;
          ctx.shadowBlur = 14;
          ctx.fillStyle = 'rgba(8, 15, 32, 0.9)';
          ctx.strokeStyle = pw.color;
          ctx.lineWidth = 2.5;
          ctx.beginPath();
          ctx.arc(0, 0, pw.r, 0, Math.PI * 2);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = pw.color;
          ctx.font = '900 13px Orbitron, sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(pw.label, 0, 1);
          ctx.restore();
        }

        // Player Bullets
        for (const b of game.bullets) {
          ctx.save();
          ctx.shadowColor = b.color;
          ctx.shadowBlur = 12;
          ctx.fillStyle = b.color;
          ctx.beginPath();
          ctx.roundRect(b.x - b.r * 0.65, b.y - b.r * 2.4, b.r * 1.3, b.r * 4.8, 4);
          ctx.fill();
          ctx.restore();
        }

        // Enemy Bullets
        for (const eb of game.enemyBullets) {
          ctx.save();
          ctx.shadowColor = eb.color;
          ctx.shadowBlur = 10;
          ctx.fillStyle = eb.color;
          ctx.beginPath();
          ctx.arc(eb.x, eb.y, eb.r, 0, Math.PI * 2);
          ctx.fill();
          ctx.fillStyle = '#ffffff';
          ctx.beginPath();
          ctx.arc(eb.x, eb.y, eb.r * 0.42, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }

        // Enemies
        for (const e of game.enemies) {
          drawEnemyShip(e);
        }

        // Player Starfighter
        if (game.player && game.mode !== 'gameover') {
          drawPlayerShip(game.player);
        }

        // Particles
        for (const pt of game.particles) {
          ctx.save();
          ctx.globalAlpha = Math.max(0, pt.life / pt.maxLife);
          ctx.fillStyle = pt.color;
          ctx.shadowColor = pt.color;
          ctx.shadowBlur = 8;
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, pt.size, 0, Math.PI * 2);
          ctx.fill();
          ctx.restore();
        }

        // Floating Texts
        for (const ft of game.floatingTexts) {
          ctx.save();
          ctx.globalAlpha = Math.min(1, ft.life * 1.3);
          ctx.fillStyle = ft.color;
          ctx.font = '800 13px Orbitron, "Noto Sans KR", sans-serif';
          ctx.textAlign = 'center';
          ctx.shadowColor = '#000000';
          ctx.shadowBlur = 6;
          ctx.fillText(ft.text, ft.x, ft.y);
          ctx.restore();
        }

        // Wave Announcement Banner
        if (game.waveBannerTimer > 0) {
          ctx.save();
          ctx.globalAlpha = Math.min(1, game.waveBannerTimer);
          ctx.fillStyle = 'rgba(6, 12, 26, 0.78)';
          ctx.strokeStyle = '#00f3ff';
          ctx.lineWidth = 1.5;
          const bw = Math.min(W - 32, 380);
          ctx.beginPath();
          ctx.roundRect(W / 2 - bw / 2, H * 0.34 - 22, bw, 44, 12);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = '#00f3ff';
          ctx.font = '900 15px "Noto Sans KR", Orbitron, sans-serif';
          ctx.textAlign = 'center';
          ctx.textBaseline = 'middle';
          ctx.fillText(game.waveBannerText, W / 2, H * 0.34);
          ctx.restore();
        }

        ctx.restore();
      }

      function drawPlayerShip(p) {
        ctx.save();
        if (p.invulnTimer > 0 && Math.floor(p.invulnTimer * 18) % 2 === 0) {
          ctx.globalAlpha = 0.45;
        }
        ctx.translate(p.x, p.y);

        // Twin Engine Thruster Flame
        const flameH = 14 + Math.random() * 10;
        ctx.fillStyle = '#00f3ff';
        ctx.shadowColor = '#00f3ff';
        ctx.shadowBlur = 14;
        ctx.beginPath();
        ctx.moveTo(-8, 14);
        ctx.lineTo(-4, 14 + flameH);
        ctx.lineTo(0, 14);
        ctx.moveTo(0, 14);
        ctx.lineTo(4, 14 + flameH);
        ctx.lineTo(8, 14);
        ctx.fill();

        // Main Sleek Delta Hull
        ctx.fillStyle = '#0c1933';
        ctx.strokeStyle = '#00f3ff';
        ctx.lineWidth = 2.4;
        ctx.beginPath();
        ctx.moveTo(0, -24);
        ctx.lineTo(22, 16);
        ctx.lineTo(8, 11);
        ctx.lineTo(0, 18);
        ctx.lineTo(-8, 11);
        ctx.lineTo(-22, 16);
        ctx.closePath();
        ctx.fill();
        ctx.stroke();

        // Glowing Cockpit Core
        ctx.fillStyle = '#00ff88';
        ctx.beginPath();
        ctx.ellipse(0, -3, 4, 9, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.restore();
      }

      function drawEnemyShip(e) {
        ctx.save();
        ctx.translate(e.x, e.y);
        ctx.shadowColor = e.color;
        ctx.shadowBlur = 14;
        ctx.strokeStyle = e.color;
        ctx.fillStyle = '#120b24';
        ctx.lineWidth = 2.2;

        if (e.type === 'scout') {
          ctx.beginPath();
          ctx.moveTo(0, 18);
          ctx.lineTo(16, -12);
          ctx.lineTo(0, -5);
          ctx.lineTo(-16, -12);
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
        } else if (e.type === 'interceptor') {
          ctx.beginPath();
          ctx.moveTo(0, 22);
          ctx.lineTo(22, 0);
          ctx.lineTo(12, -18);
          ctx.lineTo(-12, -18);
          ctx.lineTo(-22, 0);
          ctx.closePath();
          ctx.fill();
          ctx.stroke();
        } else if (e.type === 'cruiser') {
          ctx.beginPath();
          ctx.roundRect(-26, -22, 52, 44, 10);
          ctx.fill();
          ctx.stroke();
        } else if (e.type === 'boss') {
          // Dreadnought Boss Geometry
          ctx.beginPath();
          ctx.moveTo(0, 56);
          ctx.lineTo(58, 14);
          ctx.lineTo(48, -42);
          ctx.lineTo(-48, -42);
          ctx.lineTo(-58, 14);
          ctx.closePath();
          ctx.fill();
          ctx.stroke();

          // Boss Reactor Core
          ctx.fillStyle = '#ffbe0b';
          ctx.beginPath();
          ctx.arc(0, 4, 14, 0, Math.PI * 2);
          ctx.fill();

          // Boss Top Health Bar
          const barW = 96;
          const hpRatio = Math.max(0, e.hp / e.maxHp);
          ctx.fillStyle = 'rgba(0,0,0,0.75)';
          ctx.fillRect(-barW / 2, -56, barW, 7);
          ctx.fillStyle = '#ff2a85';
          ctx.fillRect(-barW / 2, -56, barW * hpRatio, 7);
        }

        ctx.restore();
      }

      /* =======================================================================
         7. HUD & EXTERNAL BUTTON CONTROLS
         ======================================================================= */
      function updateHud() {
        document.getElementById('hudScore').textContent = game.score.toLocaleString();
        document.getElementById('hudWave').textContent = game.wave;
        document.getElementById('hudCombo').textContent = `x${game.combo}`;

        if (game.player) {
          const hpPct = Math.round((game.player.hp / game.player.maxHp) * 100);
          document.getElementById('hudHpText').textContent = `${hpPct}%`;
          document.getElementById('hudHpBar').style.width = `${hpPct}%`;
        }

        const ultPct = Math.round(game.novaCharge);
        document.getElementById('hudUltText').textContent = `${ultPct}%`;
        document.getElementById('hudUltBar').style.width = `${ultPct}%`;

        const novaBtn = document.getElementById('btnNova');
        if (ultPct >= 100) {
          novaBtn.classList.add('nova-ready');
        } else {
          novaBtn.classList.remove('nova-ready');
        }
      }

      function togglePause() {
        if (game.mode === 'playing') {
          game.mode = 'paused';
          document.getElementById('btnPause').textContent = '▶️ 계속하기';
          triggerWaveBanner('GAME PAUSED (일시정지)');
        } else if (game.mode === 'paused') {
          game.mode = 'playing';
          document.getElementById('btnPause').textContent = '⏸️ 일시정지';
          game.waveBannerTimer = 0;
        }
      }

      document.getElementById('btnStartGame').addEventListener('click', () => {
        synth.unlock();
        document.getElementById('startOverlay').classList.add('hidden');
        resetGame();
      });

      document.getElementById('btnRestartGame').addEventListener('click', () => {
        synth.unlock();
        document.getElementById('gameOverOverlay').classList.add('hidden');
        resetGame();
      });

      document.getElementById('btnNova').addEventListener('click', () => {
        synth.unlock();
        activateNovaBomb();
      });

      document.getElementById('btnPause').addEventListener('click', () => {
        synth.unlock();
        togglePause();
      });

      document.getElementById('btnSound').addEventListener('click', () => {
        synth.unlock();
        const muted = synth.toggleMute();
        document.getElementById('btnSound').textContent = muted ? '🔇 사운드 OFF' : '🔊 사운드 ON';
      });

      /* =======================================================================
         8. MAIN ANIMATION LOOP (WINDOW ONLOAD)
         ======================================================================= */
      let lastTime = performance.now();

      function gameLoop(now) {
        const dt = Math.min(0.05, (now - lastTime) / 1000);
        lastTime = now;

        update(dt);
        draw();

        requestAnimationFrame(gameLoop);
      }

      window.onload = function () {
        resizeCanvas();
        initStars();
        requestAnimationFrame(gameLoop);
      };
    })();
  </script>
</body>
</html>
