import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import Reservation from '@/components/Reservation';
import TripleDate from "../components/TripleDate";
import CheckOrderStatus from "../components/CheckOrderStatus";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/hello',
      name: 'HelloWorld',
      component: HelloWorld,
    },
    {
      path: '/check',
      name: 'Check',
      component: CheckOrderStatus,
      props: true,
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
