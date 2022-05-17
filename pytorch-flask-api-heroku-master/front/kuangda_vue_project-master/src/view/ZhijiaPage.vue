<template>
    <div>
        <HeaderInfo></HeaderInfo>
        <LeftNav></LeftNav>
        <ZhijiaInfo></ZhijiaInfo>
    </div>
</template>
<script>
import HeaderInfo from '../components/HeaderInfo.vue'
import LeftNav from '../components/LeftNav.vue'
import ZhijiaInfo from '../components/ZhijiaInfo.vue'


export default {
    components: {
        HeaderInfo,
        LeftNav,
        ZhijiaInfo,
    },   
}
</script>
<style scoped>

</style>