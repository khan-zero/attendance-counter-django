const revenueChart = document.getElementById('revenueChart').getContext('2d');
const profileChart = document.getElementById('profileChart').getContext('2d');

// Revenue Chart
new Chart(revenueChart, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        datasets: [{
            label: '2023',
            data: [10, 20, 30, 40, 50, 60, 70],
            backgroundColor: '#7352ff',
            borderColor: '#7352ff',
            borderWidth: 1
        }, {
            label: '2022',
            data: [15, 25, 35, 45, 55, 65, 75],
            backgroundColor: '#e0e0e0',
            borderColor: '#e0e0e0',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

// Profile Report Chart
new Chart(profileChart, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul'],
        datasets: [{
            label: 'Growth',
            data: [20, 25, 30, 35, 40, 45, 50],
            backgroundColor: 'rgba(115, 82, 255, 0.1)',
            borderColor: '#7352ff',
            borderWidth: 2,
            fill: true
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

