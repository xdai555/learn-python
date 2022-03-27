import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import myHello from '@/components/hello'
import NotFound from '@/components/NotFound'
import Index from '@/components/Index'
import TodoList from '@/components/TodoList'

Vue.use(Router)

/*  export default命令，为模块指定默认输出。 export default 命令用于指定模块的默认输出。显然，一个模块只能有一个默认输出，因此export default命令只能使用一次。所以，import命令后面才不用加大括号，因为只可能唯一对应export default命令。   */
export default new Router({
  routes: [
    {
      path: '/hello-world',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/hello',
      name: 'my-hello',
      component: myHello
    },
    {
      path: '/goHome',
      redirect: '/'
    },
    {
      path: '/',
      component: Index
    },
    {
      path: '/todo',
      component: TodoList
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})
