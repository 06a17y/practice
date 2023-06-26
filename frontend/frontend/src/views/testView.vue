<template>
  <div class="test">
    <h1>This is an test page</h1>
    <h1>This is an test page</h1>
    <h1>This is an test page</h1>
    <el-button type="success" @click="success()">Success</el-button>
  </div>
</template>

<script>
export default {
  setup() {
    return {
      success() {
        console.log("YAAAA!");
      },
    };
  },
};
</script>
