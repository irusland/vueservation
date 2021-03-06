import Vue from 'vue';
import Router from 'vue-router';
import Reservation from '@/components/Reservation';
import CheckOrderStatus from '../components/CheckOrderStatus';
import Main from '../components/Main';
import Restaurants from '../components/Restaurants';
import Orders from '../components/Orders';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: Main,
      children: [
        { path: '', component: Restaurants },
        {
          path: 'reservation',
          name: 'Reserve',
          component: Reservation,
        },
        {
          path: 'restaurants',
          name: 'Restaurants',
          component: Restaurants,
        },
        {
          path: 'check',
          name: 'Check',
          component: CheckOrderStatus,
          props: true,
        },
        {
          path: 'orders',
          name: 'Orders',
          component: Orders,
        },
      ],
    },
  ],
});
