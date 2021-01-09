import Vue from 'vue';
import Router from 'vue-router';
import HelloWorld from '@/components/HelloWorld';
import Ping from '@/components/Ping';
import Books from '@/components/Books';
import Reservation from '@/components/Reservation';
import CheckOrderStatus from "../components/CheckOrderStatus";
import Main from "../components/Main";
import ImageHolder from "../components/ImageHolder";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      component: Main,
      children: [
        { path: '', component: HelloWorld },
        {
          path: 'reservation',
          name: 'Reserve',
          component: Reservation,
        },
        {
          path: 'restaurants',
          name: 'Restaurants',
          component: ImageHolder,
        },
        {
          path: 'check',
          name: 'Check',
          component: CheckOrderStatus,
          props: true,
        },
      ],
    },
  ],
  mode: 'history',
});
