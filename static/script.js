document.addEventListener('DOMContentLoaded', function() {
    const processButton = document.getElementById('processButton');
    const loadingIndicator = document.getElementById('loadingIndicator');
    const errorMessage = document.getElementById('errorMessage');
    const resultsSection = document.getElementById('results');

    // --- Output Elements ---
    const headOutput = document.getElementById('headOutput');
    const infoOutput = document.getElementById('infoOutput');
    const missingOutput = document.getElementById('missingOutput');
    const describeOutput = document.getElementById('describeOutput');
    const topCategoriesOutput = document.getElementById('topCategoriesOutput');
    const avgRatingCategoriesOutput = document.getElementById('avgRatingCategoriesOutput');
    const discountRatingInsight = document.getElementById('discountRatingInsight');

    /**
     * Creates a simple horizontal bar chart inside a given element.
     * @param {Object} data - The data to plot, e.g., { 'Category A': 50, 'Category B': 75 }.
     * @param {HTMLElement} element - The container element for the chart.
     * @param {string} valueLabel - A label for the value (e.g., " occurrences").
     */
    function createBarChart(data, element, valueLabel = '') {
        element.innerHTML = ''; // Clear previous content
        const maxValue = Math.max(...Object.values(data));

        for (const [key, value] of Object.entries(data)) {
            const percentage = (value / maxValue) * 100;

            const item = document.createElement('div');
            item.className = 'w-full';

            const label = document.createElement('div');
            label.className = 'flex justify-between text-sm font-medium text-slate-700 mb-1';
            label.innerHTML = `<span>${key}</span><span>${value.toLocaleString()}${valueLabel}</span>`;
            
            const barWrapper = document.createElement('div');
            barWrapper.className = 'w-full bg-slate-200 rounded-full h-2.5';
            
            const bar = document.createElement('div');
            bar.className = 'bg-blue-600 h-2.5 rounded-full';
            bar.style.width = `${percentage}%`;

            barWrapper.appendChild(bar);
            item.appendChild(label);
            item.appendChild(barWrapper);
            element.appendChild(item);
        }
    }

    processButton.addEventListener('click', async () => {
        // --- Reset UI State ---
        loadingIndicator.classList.remove('hidden');
        errorMessage.classList.add('hidden');
        resultsSection.classList.add('hidden');
        resultsSection.classList.remove('visible');

        try {
            const response = await fetch('/api/analyze');
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
            }
            const data = await response.json();

            // --- Populate the UI with new data ---
            headOutput.innerHTML = data.head;
            infoOutput.textContent = data.info;
            missingOutput.innerHTML = data.missing;
            describeOutput.innerHTML = data.describe;
            discountRatingInsight.textContent = data.discount_rating_insight;

            // Create visualizations
            createBarChart(data.top_categories, topCategoriesOutput, ' occurrences');
            createBarChart(data.avg_rating_categories, avgRatingCategoriesOutput, ' ★');

            // --- Show results ---
            resultsSection.classList.remove('hidden');
            resultsSection.classList.add('visible');

        } catch (error) {
            console.error('Analysis Error:', error);
            errorMessage.textContent = `An error occurred: ${error.message}`;
            errorMessage.classList.remove('hidden');
        } finally {
            loadingIndicator.classList.add('hidden');
        }
    });
});