document.addEventListener('DOMContentLoaded', () => {
  const logoContainer = document.querySelector('.logo-container');
  const faceContainer = document.querySelector('.face-container');
  const mainContainer = document.querySelector('.main-container');
  const face = document.querySelector('.face');
  const eyes = document.querySelectorAll('.logo-eye');
  const mouthPath = document.getElementById('mouth-path');
  const browL = document.getElementById('eyebrow-left-path');
  const browR = document.getElementById('eyebrow-right-path');
  const sound = document.getElementById('camera-sound');
  const downArrow = document.querySelector('.down-arrow');
  const flashcards = document.querySelectorAll('.flashcard');

  const expressions = ['happy', 'sad', 'angry', 'confused', 'surprised', 'neutral', 'mischievous', 'tired', 'bored'];
  const mouthPaths = {
    happy: 'M10 20 Q50 0 90 20',
    sad: 'M10 10 Q50 30 90 10',
    angry: 'M10 15 L90 15',
    confused: 'M10 15 Q30 5 50 15 Q70 25 90 15',
    surprised: 'M45 15 A5 5 0 1 1 55 15 A5 5 0 1 1 45 15',
    neutral: 'M10 15 L90 15',
    mischievous: 'M10 20 Q50 10 90 20',
    tired: 'M10 15 Q50 25 90 15',
    bored: 'M10 15 L50 15'
  };
  const eyebrowPaths = {
    happy: { left: 'M0 15 Q50 5 100 15', right: 'M0 15 Q50 5 100 15' },
    sad: { left: 'M0 5 L50 15 L100 5', right: 'M0 5 L50 15 L100 5' },
    angry: { left: 'M0 10 H100', right: 'M0 10 H100' },
    confused: { left: 'M0 15 Q50 5 100 15', right: 'M0 10 H100' },
    surprised: { left: 'M0 15 Q50 0 100 15', right: 'M0 15 Q50 0 100 15' },
    neutral: { left: 'M0 10 H100', right: 'M0 10 H100' },
    mischievous: { left: 'M0 15 Q50 5 100 15', right: 'M0 10 H100' },
    tired: { left: 'M0 5 Q50 15 100 5', right: 'M0 5 Q50 15 100 5' },
    bored: { left: 'M0 10 H100', right: 'M0 10 H100' }
  };

  let exprIndex = 0, spinCW = true;

  function applyExpression(name) {
    expressions.forEach(e => face.classList.remove(`expression-${e}`));
    face.classList.add(`expression-${name}`);
    mouthPath.setAttribute('d', mouthPaths[name]);
    browL.setAttribute('d', eyebrowPaths[name].left);
    browR.setAttribute('d', eyebrowPaths[name].right);
    document.querySelectorAll('.eyebrow').forEach(b => {
      b.classList.remove('bounce');
      void b.offsetWidth;
      b.classList.add('bounce');
    });
  }

  function nextExpression() {
    exprIndex = (exprIndex + 1) % expressions.length;
    applyExpression(expressions[exprIndex]);
  }

  function flipEyes() {
    spinCW = !spinCW;
    eyes.forEach(e => {
      e.classList.toggle('rotate-clockwise');
      e.classList.toggle('rotate-counterclockwise');
    });
  }

  function blink() {
    eyes.forEach(e => {
      e.classList.add('blinking');
      setTimeout(() => e.classList.remove('blinking'), 500);
    });
    setTimeout(blink, Math.random() * 2000 + 5000);
  }

  function sprinkleCameras() {
    console.log('📸 Adding fixed camera...');
    const cam = document.createElement('img');
    cam.src = 'cam2.png';
    cam.dataset.still = 'cam2.png';
    cam.dataset.gif = 'cam2.gif';
    cam.className = 'camera';

    cam.style.top = '23%';
    cam.style.left = '17%';
    cam.style.transform = 'rotate(-15deg)';

    cam.addEventListener('mouseenter', () => {
      cam.src = cam.dataset.gif;
      cam.classList.add('wiggle');
      sound.currentTime = 0;
      sound.play().catch(err => console.warn('🔇 Sound play failed:', err));
    });

    cam.addEventListener('animationend', () => {
      cam.classList.remove('wiggle');
    });

    cam.addEventListener('mouseleave', () => {
      cam.src = cam.dataset.still;
    });

    faceContainer.appendChild(cam);
  }

  function showFace() {
    logoContainer.style.display = 'none';
    faceContainer.style.display = 'flex';
    downArrow.style.display = 'block';
    sprinkleCameras();
    setInterval(nextExpression, 1500);
    setInterval(flipEyes, 1500);
  }

  function handleScroll() {
    const scrollPosition = window.scrollY;
    const windowHeight = window.innerHeight;

    // Hide main-container when scrolled past the first page
    if (scrollPosition > windowHeight * 0.1) {
      mainContainer.style.display = 'none';
    } else {
      mainContainer.style.display = 'block';
    }

    // Show flashcards one by one
    flashcards.forEach((card, index) => {
      const cardTop = card.offsetTop;
      if (scrollPosition > cardTop - windowHeight * 0.8) {
        card.classList.add('visible');
      }
    });
  }

  downArrow.addEventListener('click', () => {
    window.scrollTo({
      top: window.innerHeight,
      behavior: 'smooth'
    });
  });

  // Show logo initially, transition to face after zoomOut animation (2s)
  setTimeout(showFace, 2000);

  applyExpression(expressions[0]);
  eyes.forEach(e => e.classList.add('rotate-clockwise'));
  blink();
  window.addEventListener('scroll', handleScroll);
});