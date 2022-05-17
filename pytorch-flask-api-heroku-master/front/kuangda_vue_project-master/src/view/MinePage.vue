<template>
    <div>
        <HeaderInfo></HeaderInfo>
        <LeftNav></LeftNav>
        <MineInfo></MineInfo>
    </div>
</template>
<script>
import HeaderInfo from '../components/HeaderInfo.vue'
import LeftNav from '../components/LeftNav.vue'
import MineInfo from '../components/MineInfo.vue'


export default {
    components: {
        HeaderInfo,
        LeftNav,
        MineInfo,
    },
    
}
</script>
<style scoped>

</style>