// Function to load and render the scenario data and sections
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-zoom"></script>

function loadScenarioData() {
    const scenarioContainer = document.getElementById('scenario-container');

    // Loop over the scenarios (1 to 20)
    for (let i = 1; i <= 20; i++) {
        // Create the scenario block element
        const scenarioBlock = document.createElement('div');
        scenarioBlock.classList.add('scenario-block');

        // Add the title for the scenario
        const title = document.createElement('h2');
        title.innerHTML = `Scenario ${i}: Branch vs Branchless`;
        scenarioBlock.appendChild(title);

        // Create a canvas for the graph
        const graphCanvas = document.createElement('canvas');
        graphCanvas.classList.add('graph');
        scenarioBlock.appendChild(graphCanvas);

        // Add the section for the scenario content
        const section = document.createElement('section');
        const sectionContent = document.createElement('div');
        sectionContent.id = `scenario-${i}-section`;
        section.appendChild(sectionContent);
        scenarioBlock.appendChild(section);

        // Append the scenario block to the container
        scenarioContainer.appendChild(scenarioBlock);

        // Load the data and render the graph
        fetch(`data/scenario_${i}_results.json`)
            .then(response => response.json())
            .then(data => {
                renderGraph(graphCanvas, data);
            });

        // Load the section content from the HTML file
        fetch(`sections/scenario_section_${i}.html`)
            .then(response => response.text())
            .then(content => {
                document.getElementById(`scenario-${i}-section`).innerHTML = content;
            });
    }
}

// Function to render the graph for a specific scenario with advanced features
function renderGraph(canvas, data) {
    const ctx = canvas.getContext('2d');

    // Use Chart.js with advanced features
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: ['Time Point 1', 'Time Point 2'], // Modify this if your data has more time points
            datasets: [{
                label: 'Branch',
                data: data.branch,
                borderColor: 'rgba(75, 192, 192, 1)',
                fill: false,
                pointRadius: 5,
                pointBackgroundColor: 'rgba(75, 192, 192, 1)',
                pointBorderColor: '#fff',
            }, {
                label: 'Branchless',
                data: data.branchless,
                borderColor: 'rgba(153, 102, 255, 1)',
                fill: false,
                pointRadius: 5,
                pointBackgroundColor: 'rgba(153, 102, 255, 1)',
                pointBorderColor: '#fff',
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: false,
                    title: {
                        display: true,
                        text: 'Time (s)'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Time Points'
                    }
                }
            },
            plugins: {
                tooltip: {
                    enabled: true,
                    callbacks: {
                        label: function(tooltipItem) {
                            return `${tooltipItem.dataset.label}: ${tooltipItem.raw.toFixed(4)}s`;
                        }
                    }
                },
                zoom: {
                    pan: {
                        enabled: true,
                        mode: 'xy',
                    },
                    zoom: {
                        enabled: true,
                        mode: 'xy',
                        speed: 0.1
                    }
                }
            }
        }
    });
}

// Call the loadScenarioData function when the page loads
window.onload = loadScenarioData;
