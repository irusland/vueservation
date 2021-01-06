import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import Reservation from '@/components/Reservation';
import TripleDate from "../components/TripleDate";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
      path: '/td',
      name: 'HelloWorld',
      component: TripleDate,
    },
    {
      path: '/',
      component: Reservation,
    },
    {
      path: '/books',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'history',
});
