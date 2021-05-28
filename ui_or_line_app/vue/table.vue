<template>
  <div class="dashboard-container">
    <div class="dashboard-text"><h6>({{ name }})</h6></div>
    <el-table
      ref="multipleTable"
      v-loading="listLoading"
      :data="list"
      tooltip-effect="dark"
      element-loading-text="Loading"
      border
      fit
      height="700"
      highlight-current-row
      @selection-change="handleSelectionChange"
    >
      <el-table-column type="selection" width="55" />
      <el-table-column v-for="(column, idx) in tableColumns" :key="column.label" :label="column.label" :prop="column.prop">
        <template slot-scope="scope">
          <template v-if="column.t == 'text'">
            {{ scope.row[idx].v }}
          </template>
          <el-input v-if="column.t == 'input'" v-model="scope.row[idx].v" />
          <el-select v-if="column.t == 'select'" v-model="scope.row[idx].v" filterable allow-create default-first-option>
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
          <el-select v-if="column.t == 'muti_select'" v-model="scope.row[idx].v_list" multiple filterable allow-create default-first-option>
            <el-option v-for="item in options" :key="item.value" :label="item.label" :value="item.value" />
          </el-select>
          <el-tag v-if="column.t == 'tag'" :type="scope.row[idx].v | statusFilter">{{ scope.row[idx].label }}</el-tag>
          <template v-if="column.t == 'operate'">
            <el-radio-group width="210">
              <el-button type="primary" round size="small" @click="handleClickConfirm(scope.row)">确定</el-button>
              <el-button type="primary" round size="small" @click="handleClickDelete(scope.row)">删除</el-button>
              <el-button type="primary" round size="small" @click="handleClickCopy(scope.row)">复制</el-button>
            </el-radio-group>
          </template>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import { getList } from '@/api/myproject'

export default {
  name: '动态生成表格',
  filters: {
    statusFilter(status) {
      const statusMap = {
        1: 'success',
        // 待确定: 'gray',
        0: 'danger'
      }
      return statusMap[status]
    }
  },
  data() {
    return {
      listLoading: true,
      tableColumns: null,
      list: null
    }
  },
  created() {
    this.fetchData()
  },
  computed: {
    ...mapGetters([
      'name'
    ])
  },
  methods: {
    debug(...optionalParams) {
      this.debug(optionalParams)
    },
    fetchData() {
      this.listLoading = true
      getList().then(response => {
        this.page_bar.total = response.data.total
        this.tableColumns = response.data.columns
        this.list = response.data.items
        this.listLoading = false
      })
    },
    handleClickConfirm() {

    },
    handleClickDelete() {
      this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        if (!muti) {
          row = [row]
        }
        const data = {
          project_id: this.project_id,
          data: row
        }
        delete_corpus(data).then(response => {
          if (response.data.ok === 1) {
            this.debug('删除返回值: ', response)
            this.$message({
              message: '删除成功',
              type: 'success'
            })
          } else {
            this.$message({
              message: '删除失败',
              type: 'warning'
            })
          }
        })
        this.debug('删除: ', data)
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    handleClickCopy() {

    },
    handleSelectionChange(val) {
      this.debug('✅: ', val)
    }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
