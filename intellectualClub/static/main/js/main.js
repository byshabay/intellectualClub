// new Vue({
//     el: '#test',
//     data: {
//         events: []
//     },
//     created: function () {
//         const vm = this;
//         axios.get('/api/event')
//             .then(function (response) {
//                 vm.events = response.data
//             })
//     }
// })

const CounterPlus = {
    data() {
        return {
            counter: 0
        }
    },
    methods: {
        counterPlus() {
            return this.counter++
        },
        counterMinus() {
            return this.counter--
        }

    }
}

Vue.createApp(CounterPlus).mount('#counter')