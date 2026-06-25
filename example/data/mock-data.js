var MOCK = {
  orders: {
    list: [
      { id: "ORD202601010001", customer: "张三汽修", amount: 3842.50, status: "pending",   created_at: "2026-01-01 10:28" },
      { id: "ORD202601010002", customer: "李四汽车服务", amount: 15680.00, status: "pending",   created_at: "2026-01-01 14:15" },
      { id: "ORD202601010003", customer: "王五配件", amount: 238.00, status: "approved", created_at: "2026-01-01 09:00" },
      { id: "ORD202512310004", customer: "赵六汽修厂", amount: 8999.00, status: "approved", created_at: "2025-12-31 20:00" },
      { id: "ORD202512300005", customer: "孙七汽车美容", amount: 520.00, status: "rejected", created_at: "2025-12-30 15:00" },
    ],
    emptyList: [],
    searchEmpty: [],
  },
  getOrderById: function(id) {
    return this.orders.list.find(function(o) { return o.id === id; }) || null;
  },
};
