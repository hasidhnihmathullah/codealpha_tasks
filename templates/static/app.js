// Instant Category Filtering (Watches, Earphones, Bags, Bracelets)
function filterCategory(category, buttonElement) {
    const cards = document.querySelectorAll('.item-card');
    const titleHeader = document.getElementById('catalogTitle');

    // Update active button state if clicked from the filter pills
    if (buttonElement) {
        document.querySelectorAll('.pill-btn').forEach(btn => btn.classList.remove('active'));
        buttonElement.classList.add('active');
    }

    // Update Section Title
    const titles = {
        'all': 'All Featured Products',
        'watches': '⌚ Luxury Timepieces Collection',
        'earphones': '🎧 ANC Audio & Earbuds',
        'handbags': '👜 Designer Handbags & Totes',
        'bracelets': '✨ Crafted Bracelets & Jewelry'
    };
    if (titleHeader && titles[category]) {
        titleHeader.innerText = titles[category];
    }

    cards.forEach(card => {
        const title = (card.getAttribute('data-title') || '').toLowerCase();
        let matches = false;

        if (category === 'all') {
            matches = true;
        } else if (category === 'watches') {
            matches = title.includes('watch') || title.includes('chronograph');
        } else if (category === 'earphones') {
            matches = title.includes('ear') || title.includes('buds') || title.includes('airsound') || title.includes('pebble');
        } else if (category === 'handbags') {
            matches = title.includes('bag') || title.includes('tote') || title.includes('satchel');
        } else if (category === 'bracelets') {
            matches = title.includes('bracelet') || title.includes('bangle') || title.includes('cuff') || title.includes('chain set');
        }

        card.style.display = matches ? 'flex' : 'none';
    });

    // Smooth scroll down to the product catalog
    const shopSection = document.getElementById('shop');
    if (shopSection) {
        shopSection.scrollIntoView({ behavior: 'smooth' });
    }
}

// Real-Time Search Filter
function searchFilter() {
    const query = document.getElementById('storeSearch').value.toLowerCase();
    const cards = document.querySelectorAll('.item-card');
    cards.forEach(card => {
        const title = (card.getAttribute('data-title') || '').toLowerCase();
        card.style.display = title.includes(query) ? 'flex' : 'none';
    });
}

// Shopping Cart Drawer Controls
function toggleCartDrawer() {
    const drawer = document.getElementById('cartDrawer');
    const overlay = document.getElementById('drawerOverlay');
    if (drawer.classList.contains('open')) {
        drawer.classList.remove('open');
        overlay.style.display = 'none';
    } else {
        drawer.classList.add('open');
        overlay.style.display = 'block';
    }
}

// Authentication Modal Controls
function toggleAuthModal() {
    const modal = document.getElementById('authModal');
    modal.style.display = (modal.style.display === 'flex') ? 'none' : 'flex';
}

function closeAuthModal(event) {
    if (event.target.id === 'authModal') {
        document.getElementById('authModal').style.display = 'none';
    }
}

// Product Details Modal Window
function showProductDetails(name, desc, price, img, id) {
    document.getElementById('detailTitle').innerText = name;
    document.getElementById('detailDesc').innerText = desc;
    document.getElementById('detailPrice').innerText = '$' + price;
    document.getElementById('detailImg').src = img;
    document.getElementById('detailAddBtn').href = '/cart/add/' + id + '/';
    document.getElementById('detailsModal').style.display = 'flex';
}

function closeDetailsModal(event) {
    if (event.target.id === 'detailsModal') {
        document.getElementById('detailsModal').style.display = 'none';
    }
}

// Live Countdown Simulation
document.addEventListener('DOMContentLoaded', () => {
    let totalSecs = (2 * 86400) + (14 * 3600) + (36 * 60) + 22;
    const daysEl = document.getElementById('days');
    const hoursEl = document.getElementById('hours');
    const minsEl = document.getElementById('mins');
    const secsEl = document.getElementById('secs');

    if (daysEl && hoursEl && minsEl && secsEl) {
        setInterval(() => {
            if (totalSecs > 0) {
                totalSecs--;
                const d = Math.floor(totalSecs / 86400);
                const h = Math.floor((totalSecs % 86400) / 3600);
                const m = Math.floor((totalSecs % 3600) / 60);
                const s = totalSecs % 60;

                daysEl.innerText = String(d).padStart(2, '0');
                hoursEl.innerText = String(h).padStart(2, '0');
                minsEl.innerText = String(m).padStart(2, '0');
                secsEl.innerText = String(s).padStart(2, '0');
            }
        }, 1000);
    }
});