// Contact Form
document.getElementById('contactForm').onsubmit = function(e) {
  e.preventDefault();
  const data = Object.fromEntries(new FormData(e.target));
  fetch('/contact/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  }).then(() => {
    alert('Message sent!');
    e.target.reset();
  }).catch(() => alert('Failed to send message.'));
};

// Newsletter Form
document.getElementById('subscribeForm').onsubmit = function(e) {
  e.preventDefault();
  const email = e.target.email.value;
  fetch('/subscribe/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email })
  }).then(() => {
    alert('Subscribed successfully!');
    e.target.reset();
  }).catch(() => alert('Subscription failed.'));
};

// Reveal sections on scroll
const sections = document.querySelectorAll('.section');

const revealOnScroll = () => {
  const triggerBottom = window.innerHeight * 0.85;
  sections.forEach(section => {
    const top = section.getBoundingClientRect().top;
    if (top < triggerBottom) {
      section.classList.add('visible');
    }
  });
};

window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);
