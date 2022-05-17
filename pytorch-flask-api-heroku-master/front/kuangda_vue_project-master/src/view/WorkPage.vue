<template>
    <div>
        <HeaderInfo></HeaderInfo>
        <LeftNav></LeftNav>
        <WorkInfo></WorkInfo>
    </div>
</template>
<script>
import HeaderInfo from '../components/HeaderInfo.vue'
import LeftNav from '../components/LeftNav.vue'
import WorkInfo from '../components/WorkInfo.vue'


export default {
    components: {
        HeaderInfo,
        LeftNav,
        WorkInfo,
    },
    
}
</script>
<style scoped>

</style>