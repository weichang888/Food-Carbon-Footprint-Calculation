document.addEventListener('DOMContentLoaded', function() {
    const quantityInputs = document.querySelectorAll('input[type="number"]');

    quantityInputs.forEach(input => {
        input.addEventListener('input', function() {
            const carbonFootprint = parseFloat(this.dataset.carbonFootprint);
            const quantity = parseFloat(this.value);
            const totalCarbon = carbonFootprint * quantity;

            // 查找并显示总碳足迹的元素，而不是按钮
            const totalCarbonElement = this.parentElement.querySelector('.total-carbon');
            if (!isNaN(totalCarbon)) {
                totalCarbonElement.textContent = `總碳足跡: ${totalCarbon.toFixed(2)} kg CO2e`;
            } else {
                totalCarbonElement.textContent = '';
            }
        });
    });
});
