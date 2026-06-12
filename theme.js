// Theme Toggle & Persistence
document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('themeToggle');
    if (themeToggleBtn) {
        // Determine initial theme
        const storedTheme = localStorage.getItem('evx-theme');
        const prefersLight = window.matchMedia('(prefers-color-scheme: light)').matches;
        
        if (storedTheme === 'light' || (!storedTheme && prefersLight)) {
            document.documentElement.setAttribute('data-theme', 'light');
        }

        themeToggleBtn.addEventListener('click', () => {
            const isLight = document.documentElement.getAttribute('data-theme') === 'light';
            if (isLight) {
                document.documentElement.removeAttribute('data-theme');
                localStorage.setItem('evx-theme', 'dark');
            } else {
                document.documentElement.setAttribute('data-theme', 'light');
                localStorage.setItem('evx-theme', 'light');
            }
        });
    }

    // GSAP ScrollTrigger Animations
    if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Fade up reveals
        gsap.utils.toArray('.reveal').forEach(el => {
            gsap.fromTo(el, 
                { y: 48, opacity: 0 },
                {
                    scrollTrigger: {
                        trigger: el,
                        start: "top 85%",
                        toggleActions: "play none none reverse"
                    },
                    y: 0,
                    opacity: 1,
                    duration: 0.9,
                    ease: "power3.out"
                }
            );
        });

        // Staggered child reveals
        gsap.utils.toArray('.stagger-parent').forEach(parent => {
            const children = parent.querySelectorAll('.stagger-child');
            if (children.length > 0) {
                gsap.fromTo(children, 
                    { y: 48, opacity: 0 },
                    {
                        scrollTrigger: {
                            trigger: parent,
                            start: "top 85%",
                            toggleActions: "play none none reverse"
                        },
                        y: 0,
                        opacity: 1,
                        duration: 0.8,
                        stagger: 0.1,
                        ease: "power3.out"
                    }
                );
            }
        });
    }

    // Three.js Hero
    const heroCanvas = document.getElementById('webgl-hero');
    if (heroCanvas && typeof THREE !== 'undefined' && window.innerWidth >= 768) {
        const scene = new THREE.Scene();
        
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 30;

        const renderer = new THREE.WebGLRenderer({ canvas: heroCanvas, alpha: true, antialias: true });
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));

        const particlesGeometry = new THREE.BufferGeometry();
        const particlesCount = 700;
        const posArray = new Float32Array(particlesCount * 3);

        for(let i = 0; i < particlesCount * 3; i++) {
            posArray[i] = (Math.random() - 0.5) * 100;
        }

        particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
        
        const isLight = document.documentElement.getAttribute('data-theme') === 'light';
        const materialColor = isLight ? 0x0e7490 : 0x67e8f9;

        const particlesMaterial = new THREE.PointsMaterial({
            size: 0.15,
            color: materialColor,
            transparent: true,
            opacity: 0.8,
            blending: THREE.AdditiveBlending
        });

        const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
        scene.add(particlesMesh);

        let mouseX = 0;
        let mouseY = 0;

        window.addEventListener('mousemove', (event) => {
            mouseX = (event.clientX / window.innerWidth) - 0.5;
            mouseY = -(event.clientY / window.innerHeight) + 0.5;
        });

        // Handle theme change for particles color
        if (themeToggleBtn) {
            themeToggleBtn.addEventListener('click', () => {
                const currentLight = document.documentElement.getAttribute('data-theme') === 'light';
                particlesMaterial.color.setHex(currentLight ? 0x0e7490 : 0x67e8f9);
                particlesMaterial.blending = currentLight ? THREE.NormalBlending : THREE.AdditiveBlending;
                particlesMaterial.needsUpdate = true;
            });
        }

        window.addEventListener('resize', () => {
            if(window.innerWidth < 768) {
                heroCanvas.style.display = 'none';
            } else {
                heroCanvas.style.display = 'block';
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            }
        });

        const clock = new THREE.Clock();

        function animate() {
            requestAnimationFrame(animate);
            const elapsedTime = clock.getElapsedTime();

            particlesMesh.rotation.y = elapsedTime * 0.05;
            particlesMesh.rotation.x = elapsedTime * 0.02;

            camera.position.x += (mouseX * 10 - camera.position.x) * 0.05;
            camera.position.y += (mouseY * 10 - camera.position.y) * 0.05;
            camera.lookAt(scene.position);

            renderer.render(scene, camera);
        }
        animate();
    } else if (heroCanvas) {
        // Hide canvas on mobile or if Three.js not loaded
        heroCanvas.style.display = 'none';
    }
});
