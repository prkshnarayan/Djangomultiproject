//// Global variables
//let currentPlaylist = [];
//let currentSongIndex = 0;
//let currentArtist = null;
//let isArtistPage = false;
//
//// Audio elements
//const audioPlayer = document.getElementById('song');
//const progressBar = document.getElementById('progress');
//const controlIcon = document.getElementById('controlIcon');
//const nowPlayingTitle = document.getElementById('nowPlayingTitle');
//const nowPlayingArtist = document.getElementById('nowPlayingArtist');
//const rotatingImage = document.getElementById('rotatingImage');
//
//// Recommended songs data (should match your HTML)
//const recommendedSongs = [
//    {
//        title: "Tharagathi Gadhi",
//        artist: "Kaala Bhairava",
//        source: "/static/audio/recommend/Tharagathi Gadhi.mp3",
//        cover: "/static/images/recmnd1.jpg",
//        duration: "4:33"
//    },
//    {
//        title: "Nee Chitram Choosi",
//        name: "Anurag Kulkarni",
//        source: "/static/audio/recommend/[iSongs.info] 02 - Nee Chitram Choosi.mp3",
//        cover: "/static/images/recmnd2.jpg",
//        duration: "4:33"
//    },
//    {
//       title: "Niddura Potunna",
//       name: "Shankar Mahadevan Garu",
//       source: "/static/audio/recommend/[iSongs.info] 05 - Niddura Pothunna.mp3",
//       cover: "/static/images/recmnd3.jpg",
//       duration: "4:33"
//    },
//    {
//       title: "Niluvadhamu Ninu Epudaina",
//       name: "Karthik & Sumangali",
//       source: "/static/audio/recommend/[iSongs.info] 01 - Niluvadhamu Ninu Epudaina.mp3",
//       cover: "/static/images/recmnd4.jpg",
//       duration: "4:33"
//    },
//    {
//       title: "Idhedho Bagundhe",
//       name: "Vijay Prakash & Anitha Karthikeyan",
//       source: "/static/audio/recommend/[iSongs.info] 03 - Idhedho Bagundhe.mp3",
//       cover: "/static/images/recmnd5.jpg",
//       duration: "4:33"
//    },
//    {
//       title: "Konte Chooputho",
//       name: "Belly Raj, Deepa Mariam",
//       source: "/static/audio/recommend/[iSongs.info] 01 - Konte Chooputho.mp3",
//       cover: "/static/images/recmnd6.jpg",
//       duration: "4:33"
//    },
//    {
//       title: "Chirunama Thana Chirunama",
//       name: "Yazin Nizar",
//       source: "/static/audio/recommend/[iSongs.info] 01 - Chirunama Thana Chirunama.mp3",
//       cover: "/static/images/recmnd7.jpg",
//       duration: "4:33"
//    },
//    {
//       title: "Nuvvu Navvukuntu",
//       name: "Kapil Kapilan",
//       source: "/static/audio/recommend/[iSongs.info] 02 - Nuvvu Navvukuntu.mp3",
//       cover: "/static/images/recmnd8.jpg",
//       duration: "4:33"
//    },
//    {
//       title: "Pranam Kanna",
//       name: "Kailash Kher",
//       source: "/static/audio/recommend/Pranam Kanna - InstaSong.In.mp3",
//       cover: "/static/images/recmnd10.jpg",
//       duration: "4:33"
//    },
//];
//
//// Function to detect current artist from URL
//function detectCurrentArtist() {
//    const path = window.location.pathname;
//    const artistMap = {
//        'anurag_kulkarni': 'Anurag Kulkarni',
//        'dsp': 'D.S.P',
//        'geetha_madhuri': 'Geetha Madhuri',
//        'k_s_chitra': 'K.S. Chitra',
//        'ramya_behara': 'Ramya Behara',
//        'shreya_goshal': 'Shreya Ghoshal',
//        'sid_sriram': 'Sid Sriram',
//        'sunitha': 'Sunitha Upadrashta',
//        'pakash':'Prakash',
//    };
//
//    for (const [pathPart, artist] of Object.entries(artistMap)) {
//        if (path.includes(pathPart)) {
//            isArtistPage = true;
//            return artist;
//        }
//    }
//    isArtistPage = false;
//    return null;
//}
//
//// Function to setup artist playlist
//function setupArtistPlaylist() {
//    currentArtist = detectCurrentArtist();
//    currentPlaylist = [];
//
//    if (isArtistPage) {
//        const songItems = document.querySelectorAll('.song-list .song-item');
//
//        songItems.forEach((item, index) => {
//            const title = item.querySelector('.song-title').textContent;
//            const duration = item.querySelector('.song-duration').textContent;
//
//            // For Anurag Kulkarni page which has <a> tags
//            const link = item.closest('a');
//            const source = link ? link.getAttribute('href') :
//                `/static/audio/${currentArtist.replace(/\s+/g, '_')}/${title.replace(/\s+/g, '_')}.mp3`;
//
//            currentPlaylist.push({
//                title: title,
//                artist: currentArtist,
//                source: source,
//                duration: duration,
//                cover: document.querySelector('.artist-image').src
//            });
//
//            // Add click handler
//            const clickable = link || item;
//            clickable.addEventListener('click', (e) => {
//                e.preventDefault();
//                playSong(index, true);
//            });
//        });
//    } else {
//        // For non-artist pages (main page with recommended songs)
//        currentPlaylist = [...recommendedSongs];
//    }
//}
//
//// Function to play song
//function playSong(index, isArtistSong = false) {
//    if (!currentPlaylist.length || index >= currentPlaylist.length) return;
//
//    currentSongIndex = index;
//    const song = currentPlaylist[index];
//
//    // Update player UI
//    nowPlayingTitle.textContent = song.title;
//    nowPlayingArtist.textContent = song.artist;
//    rotatingImage.src = song.cover;
//
//    // Set audio source
//    audioPlayer.src = song.source;
//    audioPlayer.play();
//
//    // Update controls
//    controlIcon.classList.remove('fa-play');
//    controlIcon.classList.add('fa-pause');
//    startRotation();
//
//    // Highlight active song
//    if (isArtistSong) {
//        document.querySelectorAll('.song-item').forEach((el, i) => {
//            el.classList.toggle('active', i === index);
//        });
//    } else {
//        document.querySelectorAll('.song-container .song').forEach((el, i) => {
//            el.classList.toggle('active', i === index);
//        });
//    }
//}
//
//// Setup recommended songs click handlers
//function setupRecommendedSongs() {
//    document.querySelectorAll('.song-container .song').forEach((songEl, index) => {
//        songEl.addEventListener('click', () => {
//            playSong(index);
//        });
//    });
//}
//
//// When song ends, play next
//audioPlayer.addEventListener('ended', function() {
//    if (currentPlaylist.length) {
//        const nextIndex = (currentSongIndex + 1) % currentPlaylist.length;
//        playSong(nextIndex, isArtistPage);
//    }
//});
//
//// Player controls
//document.querySelector('.play-pause-btn').addEventListener('click', function() {
//    if (audioPlayer.paused) {
//        audioPlayer.play();
//        controlIcon.classList.remove('fa-play');
//        controlIcon.classList.add('fa-pause');
//        startRotation();
//    } else {
//        audioPlayer.pause();
//        controlIcon.classList.remove('fa-pause');
//        controlIcon.classList.add('fa-play');
//        pauseRotation();
//    }
//});
//
//// Progress bar update
//audioPlayer.addEventListener('timeupdate', function() {
//    if (!audioPlayer.paused) {
//        progressBar.value = (audioPlayer.currentTime / audioPlayer.duration) * 100;
//    }
//});
//
//// Seek functionality
//progressBar.addEventListener('input', function() {
//    const seekTime = (progressBar.value / 100) * audioPlayer.duration;
//    audioPlayer.currentTime = seekTime;
//});
//
//// Initialize when page loads
//document.addEventListener('DOMContentLoaded', function() {
//    setupArtistPlaylist();
//    setupRecommendedSongs();
//
//    // For DSP page specifically - ensure songs are properly linked
//    if (window.location.pathname.includes('dsp')) {
//        const songItems = document.querySelectorAll('.song-list .song-item');
//        songItems.forEach(item => {
//            item.style.cursor = 'pointer';
//        });
//    }
//});
//
//
//
//
//
//
//
//
//
//// Modify the songItems.forEach loop in setupArtistPlaylist()
//songItems.forEach((item, index) => {
//    const title = item.querySelector('.song-title').textContent;
//    const duration = item.querySelector('.song-duration').textContent;
//
//    // Check for data-source attribute first
//    let source = item.getAttribute('data-source');
//
//    // If no data-source, try closest <a> tag (for Anurag page)
//    if (!source) {
//        const link = item.closest('a');
//        source = link ? link.getAttribute('href') :
//            `/static/audio/${currentArtist.replace(/\s+/g, '_')}/${title.replace(/\s+/g, '_')}.mp3`;
//    }
//
//    currentPlaylist.push({
//        title: title,
//        artist: currentArtist,
//        source: source,
//        duration: duration,
//        cover: document.querySelector('.artist-image').src
//    });
//
//    // Add click handler
//    item.addEventListener('click', (e) => {
//        e.preventDefault();
//        playSong(index, true);
//    });
//});







//
//
//// Global variables
//let currentPlaylist = [];
//let currentSongIndex = 0;
//let currentArtist = null;
//let isArtistPage = false;
//
//// Audio elements
//const audioPlayer = document.getElementById('song');
//const progressBar = document.getElementById('progress');
//const controlIcon = document.getElementById('controlIcon');
//const nowPlayingTitle = document.getElementById('nowPlayingTitle');
//const nowPlayingArtist = document.getElementById('nowPlayingArtist');
//const rotatingImage = document.getElementById('rotatingImage');
//
//// Function to detect current artist from page
//function detectCurrentArtist() {
//    const artistNameElement = document.querySelector('.artist-name');
//    return artistNameElement ? artistNameElement.textContent : null;
//}
//
//// Function to setup artist playlist from Django template
//function setupArtistPlaylist() {
//    currentArtist = detectCurrentArtist();
//    currentPlaylist = [];
//
//    const songItems = document.querySelectorAll('.song-list .song-item');
//
//    songItems.forEach((item, index) => {
//        const title = item.querySelector('.song-title').textContent;
//        const duration = item.querySelector('.song-duration').textContent;
//        let fileUrl = item.getAttribute('data-url'); // Try to get from data-url
//        if (!fileUrl && item.closest('a')) {
//            fileUrl = item.closest('a').getAttribute('href'); // Fallback to href if wrapped in <a>
//}
//        const coverImage = document.querySelector('.artist-image').src;
//
//        currentPlaylist.push({
//            title: title,
//            artist: currentArtist,
//            source: fileUrl,
//            duration: duration,
//            cover: coverImage
//        });
//
//        // Add click handler
//        item.style.cursor = 'pointer';
//        item.addEventListener('click', (e) => {
//            e.preventDefault();
//            playSong(index);
//        });
//    });
//}
//
//// Function to play song
//function playSong(index) {
//    if (!currentPlaylist.length || index >= currentPlaylist.length) return;
//
//    currentSongIndex = index;
//    const song = currentPlaylist[index];
//
//    // Update player UI
//    nowPlayingTitle.textContent = song.title;
//    nowPlayingArtist.textContent = song.artist;
//    rotatingImage.src = song.cover;
//
//    // Set audio source and play
//    audioPlayer.src = song.source;
//    audioPlayer.play()
//        .then(() => {
//            controlIcon.classList.remove('fa-play');
//            controlIcon.classList.add('fa-pause');
//            startRotation();
//        })
//        .catch(error => {
//            console.error('Error playing song:', error);
//        });
//
//    // Highlight active song
//    document.querySelectorAll('.song-item').forEach((el, i) => {
//        el.classList.toggle('active', i === index);
//    });
//}
//
//// Rotation functions
//let rotationInterval;
//function startRotation() {
//    if (rotationInterval) clearInterval(rotationInterval);
//    let rotation = 0;
//    rotationInterval = setInterval(() => {
//        rotation = (rotation + 1) % 360;
//        rotatingImage.style.transform = `rotate(${rotation}deg)`;
//    }, 50);
//}
//
//function pauseRotation() {
//    clearInterval(rotationInterval);
//}
//
//// Player controls
//document.querySelector('.play-pause-btn').addEventListener('click', function() {
//    if (audioPlayer.paused) {
//        audioPlayer.play();
//        controlIcon.classList.remove('fa-play');
//        controlIcon.classList.add('fa-pause');
//        startRotation();
//    } else {
//        audioPlayer.pause();
//        controlIcon.classList.remove('fa-pause');
//        controlIcon.classList.add('fa-play');
//        pauseRotation();
//    }
//});
//
//// Progress bar update
//audioPlayer.addEventListener('timeupdate', function() {
//    if (!isNaN(audioPlayer.duration)) {
//        progressBar.value = (audioPlayer.currentTime / audioPlayer.duration) * 100;
//    }
//});
//
//// Seek functionality
//progressBar.addEventListener('input', function() {
//    const seekTime = (progressBar.value / 100) * audioPlayer.duration;
//    audioPlayer.currentTime = seekTime;
//});
//
//// When song ends, play next
//audioPlayer.addEventListener('ended', function() {
//    if (currentPlaylist.length) {
//        const nextIndex = (currentSongIndex + 1) % currentPlaylist.length;
//        playSong(nextIndex);
//    }
//});
//
//// Forward/backward buttons
//document.querySelector('.forward').addEventListener('click', function() {
//    if (currentPlaylist.length) {
//        const nextIndex = (currentSongIndex + 1) % currentPlaylist.length;
//        playSong(nextIndex);
//    }
//});
//
//document.querySelector('.backward').addEventListener('click', function() {
//    if (currentPlaylist.length) {
//        const prevIndex = (currentSongIndex - 1 + currentPlaylist.length) % currentPlaylist.length;
//        playSong(prevIndex);
//    }
//});
//
//// Initialize when page loads
//document.addEventListener('DOMContentLoaded', function() {
//    setupArtistPlaylist();
//
//    // Set default cover image
//    rotatingImage.src = document.querySelector('.artist-image').src;
//
//    // Initialize progress bar
//    progressBar.value = 0;
//});
















// Global variables
let currentPlaylist = [];
let currentSongIndex = 0;
let currentArtist = null;

// Audio elements
const audioPlayer = document.getElementById('song');
const progressBar = document.getElementById('progress');
const controlIcon = document.getElementById('controlIcon');
const nowPlayingTitle = document.getElementById('nowPlayingTitle');
const nowPlayingArtist = document.getElementById('nowPlayingArtist');
const rotatingImage = document.getElementById('rotatingImage');

// Detect current artist from page
function detectCurrentArtist() {
    const artistNameElement = document.querySelector('.artist-name');
    return artistNameElement ? artistNameElement.textContent : null;
}

// Setup artist playlist
function setupArtistPlaylist() {
    currentArtist = detectCurrentArtist() || 'Unknown Artist';
    currentPlaylist = [];

    const songItems = document.querySelectorAll('.song-list .song-item');

    songItems.forEach((item, index) => {
        const title = item.querySelector('.song-title')?.textContent || 'Unknown Title';
        const duration = item.querySelector('.song-duration')?.textContent || '0:00';
        let fileUrl = item.getAttribute('data-url') || item.closest('a')?.getAttribute('href');
        const coverImage = document.querySelector('.artist-image')?.src || '';

        if (!fileUrl) {
            console.warn(`Missing data-url or href for artist song at index ${index}`);
            return;
        }

        currentPlaylist.push({
            title: title,
            artist: currentArtist,
            source: fileUrl,
            duration: duration,
            cover: coverImage
        });

        item.style.cursor = 'pointer';
        item.addEventListener('click', (e) => {
            e.preventDefault();
            playSong(index);
        });
    });
}



// Setup recommended songs
function setupRecommendedSongs() {
    const songItems = document.querySelectorAll('.recommended-songs .song');

    // Clear playlist and set it freshly
    currentPlaylist = [];

    songItems.forEach((item, index) => {
        const title = item.querySelector('h2')?.textContent || 'Unknown Title';
        const artist = item.querySelector('p')?.textContent || 'Unknown Artist';
        const duration = item.querySelector('span')?.textContent || '0:00';
        const fileUrl = item.getAttribute('data-url');
        const coverImage = item.querySelector('img')?.src || '';

        if (!fileUrl) {
            console.warn(`Missing data-url for recommended song at index ${index}`);
            return;
        }

        // Add to playlist
        currentPlaylist.push({
            title: title,
            artist: artist,
            source: fileUrl,
            duration: duration,
            cover: coverImage
        });

        // Click to play song
        item.style.cursor = 'pointer';
        item.addEventListener('click', (e) => {
            e.preventDefault();
            playSong(index); // play from currentPlaylist
        });
    });
}


// Play song by index
function playSong(index) {
    if (!currentPlaylist.length || index >= currentPlaylist.length) return;

    currentSongIndex = index;
    const song = currentPlaylist[index];

    nowPlayingTitle.textContent = song.title;
    nowPlayingArtist.textContent = song.artist;
    rotatingImage.src = song.cover;

    audioPlayer.src = song.source;
    audioPlayer.play().then(() => {
        controlIcon.classList.remove('fa-play');
        controlIcon.classList.add('fa-pause');
        startRotation();
    }).catch(err => console.error('Error playing:', err));

    document.querySelectorAll('.song-item, .recommended-songs .song').forEach((el, i) => {
        el.classList.toggle('active', i === index);
    });
}

// Rotation animation
let rotationInterval;
function startRotation() {
    if (rotationInterval) clearInterval(rotationInterval);
    let rotation = 0;
    rotationInterval = setInterval(() => {
        rotation = (rotation + 1) % 360;
        rotatingImage.style.transform = `rotate(${rotation}deg)`;
    }, 50);
}
function pauseRotation() {
    clearInterval(rotationInterval);
}

// Play/pause button
document.querySelector('.play-pause-btn').addEventListener('click', () => {
    if (audioPlayer.paused) {
        audioPlayer.play();
        controlIcon.classList.remove('fa-play');
        controlIcon.classList.add('fa-pause');
        startRotation();
    } else {
        audioPlayer.pause();
        controlIcon.classList.remove('fa-pause');
        controlIcon.classList.add('fa-play');
        pauseRotation();
    }
});

// Progress bar update
audioPlayer.addEventListener('timeupdate', () => {
    if (!isNaN(audioPlayer.duration)) {
        progressBar.value = (audioPlayer.currentTime / audioPlayer.duration) * 100;
    }
});

// Seek song
progressBar.addEventListener('input', () => {
    const seekTime = (progressBar.value / 100) * audioPlayer.duration;
    audioPlayer.currentTime = seekTime;
});

// Song end: play next
audioPlayer.addEventListener('ended', () => {
    if (currentPlaylist.length) {
        const nextIndex = (currentSongIndex + 1) % currentPlaylist.length;
        playSong(nextIndex);
    }
});

// Forward/backward controls
document.querySelector('.forward').addEventListener('click', () => {
    if (currentPlaylist.length) {
        const nextIndex = (currentSongIndex + 1) % currentPlaylist.length;
        playSong(nextIndex);
    }
});
document.querySelector('.backward').addEventListener('click', () => {
    if (currentPlaylist.length) {
        const prevIndex = (currentSongIndex - 1 + currentPlaylist.length) % currentPlaylist.length;
        playSong(prevIndex);
    }
});



document.addEventListener('DOMContentLoaded', () => {
    currentPlaylist = [];

    const artistSongsExist = document.querySelector('.song-list .song-item');
    const recommendedSongsExist = document.querySelector('.recommended-songs .song');

    if (artistSongsExist) {
        setupArtistPlaylist();
    } else if (recommendedSongsExist) {
        setupRecommendedSongs();
    }

    rotatingImage.src = document.querySelector('.album-cover img')?.src || '';
    progressBar.value = 0;
});


var swiper = new Swiper(".swiper", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  loop: true,
  speed: 600,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 10,
    stretch: 120,
    depth: 200,
    modifier: 1,
    slideShadows: false,
  },
  on: {
    click(event)
    {
      swiper.slideTo(this.clickedIndex);
    },
  },
  pagination: {
    el: ".swiper-pagination",
  },
});
