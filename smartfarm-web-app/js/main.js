// ═══════════════════════════════════════
// SmartFarm — Main JavaScript
// ═══════════════════════════════════════

// ── Mobile Menu Toggle ──
const menuBtn = document.getElementById("menu-btn");
const navbar = document.getElementById("navbar");

if (menuBtn && navbar) {
  menuBtn.addEventListener("click", () => {
    menuBtn.classList.toggle("active");
    navbar.classList.toggle("active");
  });

  // Close menu on scroll
  window.addEventListener("scroll", () => {
    menuBtn.classList.remove("active");
    navbar.classList.remove("active");
  });

  // Close menu when a link is clicked
  navbar.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      menuBtn.classList.remove("active");
      navbar.classList.remove("active");
    });
  });
}

// ── Header Scroll Effect ──
const header = document.getElementById("header");
if (header) {
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      header.classList.add("scrolled");
    } else {
      header.classList.remove("scrolled");
    }
  });
}

// ── Scroll Reveal for Showcase Rows ──
const observerOptions = {
  threshold: 0.15,
  rootMargin: "0px 0px -50px 0px",
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll(".showcase-row").forEach((row) => {
  observer.observe(row);
});

// ── Floating Particles in Hero (subtle) ──
const particlesContainer = document.getElementById("particles");
if (particlesContainer) {
  for (let i = 0; i < 20; i++) {
    const particle = document.createElement("div");
    particle.style.cssText = `
      position: absolute;
      width: ${Math.random() * 4 + 2}px;
      height: ${Math.random() * 4 + 2}px;
      background: rgba(255,255,255, ${Math.random() * 0.15 + 0.05});
      border-radius: 50%;
      top: ${Math.random() * 100}%;
      left: ${Math.random() * 100}%;
      animation: float-particle ${Math.random() * 8 + 6}s ease-in-out infinite;
      animation-delay: ${Math.random() * 4}s;
    `;
    particlesContainer.appendChild(particle);
  }

  // Inject keyframes for particles
  const style = document.createElement("style");
  style.textContent = `
    @keyframes float-particle {
      0%, 100% { transform: translateY(0) translateX(0); opacity: 0.3; }
      25% { transform: translateY(-30px) translateX(15px); opacity: 0.8; }
      50% { transform: translateY(-50px) translateX(-10px); opacity: 0.5; }
      75% { transform: translateY(-20px) translateX(20px); opacity: 0.7; }
    }
  `;
  document.head.appendChild(style);
}
