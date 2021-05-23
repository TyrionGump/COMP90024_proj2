var language_c2 = echarts.init(document.getElementById("language_c2"));
var language_c2_option = {
    legend: {},
    tooltip: {},
    dataset: {
        source: [
            ['product', '2012', '2013', '2014', '2015', '2016', '2017'],
            ['Milk Tea', 86.5, 92.1, 85.7, 83.1, 73.4, 55.1],
            ['Matcha Latte', 41.1, 30.4, 65.1, 53.3, 83.8, 98.7],
            ['Cheese Cocoa', 24.1, 67.2, 79.5, 86.4, 65.2, 82.5],
            ['Walnut Brownie', 55.2, 67.1, 69.2, 72.4, 53.9, 39.1]
        ]
    },
    series: [{
        type: 'pie',
        radius: '20%',
        center: ['20%', '30%']
        // No encode specified, by default, it is '2012'.
    }, {
        type: 'pie',
        radius: '20%',
        center: ['40%', '30%'],
        encode: {
            itemName: 'product',
            value: '2013'
        }
    }, {
        type: 'pie',
        radius: '20%',
        center: ['60%', '30%'],
        encode: {
            itemName: 'product',
            value: '2014'
        }
    }, {
        type: 'pie',
        radius: '20%',
        center: ['80%', '30%'],
        encode: {
            itemName: 'product',
            value: '2015'
        }
    }, {
        type: 'pie',
        radius: '20%',
        center: ['20%', '75%'],
        encode: {
            itemName: 'product',
            value: '2013'
        }
    }, {
        type: 'pie',
        radius: '20%',
        center: ['40%', '75%'],
        encode: {
            itemName: 'product',
            value: '2013'
        }
    }, {
        type: 'pie',
        radius: '20%',
        center: ['60%', '75%'],
        encode: {
            itemName: 'product',
            value: '2013'
        }
    }, {
        type: 'pie',
        radius: '20%',
        center: ['80%', '75%'],
        encode: {
            itemName: 'product',
            value: '2013'
        }
    },]
};
language_c2.setOption(language_c2_option);
window.addEventListener('resize', function() {
	language_c2.resize()
})