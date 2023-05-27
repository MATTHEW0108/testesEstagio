<template>
  <form action="consulta.py" method = "GET">
    <input type = "text" name = "data">
    <button type = "submit" >Buscar</button>
  </form>
</template>





<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>


