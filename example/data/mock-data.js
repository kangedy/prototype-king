var MOCK = {
  getOrders: function() {
    return [
      { id:"o1", order_no:"ORD202601010001", customer:"鑫盛汽修厂",   amount:3842.50, status:"pending",   created_at:"2026-01-01 10:28" },
      { id:"o2", order_no:"ORD202601010002", customer:"宏达汽车服务", amount:15680.00, status:"pending",   created_at:"2026-01-01 14:15" },
      { id:"o3", order_no:"ORD202601010003", customer:"永丰配件商行", amount:238.00,   status:"approved",  created_at:"2026-01-01 09:00" },
      { id:"o4", order_no:"ORD202512310004", customer:"顺达汽修厂",   amount:8999.00,  status:"shipped",   created_at:"2025-12-31 20:00" },
      { id:"o5", order_no:"ORD202512300005", customer:"捷诚汽车美容", amount:520.00,   status:"completed", created_at:"2025-12-30 15:00" },
      { id:"o6", order_no:"ORD202512280006", customer:"华胜汽配连锁", amount:12500.00, status:"completed", created_at:"2025-12-28 11:30" },
      { id:"o7", order_no:"ORD202512250007", customer:"恒通运输公司", amount:3420.00,  status:"completed", created_at:"2025-12-25 16:45" },
      { id:"o8", order_no:"ORD202512200008", customer:"众合维修中心", amount:7680.00,  status:"cancelled", created_at:"2025-12-20 09:10" },
    ];
  },
  getOrderById: function(id) {
    var list = this.getOrders();
    for (var i = 0; i < list.length; i++) {
      if (list[i].id === id) return list[i];
    }
    return null;
  },
  getProducts: function() {
    return [
      { name:"发动机总成 EA888 Gen3", category:"发动机", oe:"06H103064C", price:3850.00, stock:3,  status:"上架" },
      { name:"7速湿式双离合变速箱",   category:"变速箱", oe:"0CK300012A", price:5200.00, stock:1,  status:"上架" },
      { name:"ABS泵总成",             category:"电子电器", oe:"5Q0614517C",price:1280.00, stock:5,  status:"上架" },
      { name:"前保险杠骨架",          category:"车身件", oe:"5GD807217",  price:680.00,  stock:8,  status:"上架" },
      { name:"散热器风扇总成",        category:"电子电器", oe:"1K0959455L",price:360.00,  stock:12, status:"上架" },
      { name:"涡轮增压器 K03",        category:"发动机", oe:"06K145702H", price:2800.00, stock:0,  status:"下架" },
      { name:"发电机 14V 180A",       category:"电子电器", oe:"06F903023B",price:720.00,  stock:6,  status:"上架" },
      { name:"后桥总成",              category:"车身件", oe:"5Q0501111",  price:1800.00, stock:2,  status:"上架" },
    ];
  },
  getCustomers: function() {
    return [
      { name:"鑫盛汽修厂",   contact:"张伟",   phone:"139****8001", total:45280.00, reg_date:"2025-06-15", status:"active" },
      { name:"宏达汽车服务", contact:"李强",   phone:"138****5678", total:128500.00,reg_date:"2025-03-20", status:"active" },
      { name:"永丰配件商行", contact:"王芳",   phone:"136****9012", total:8650.00,  reg_date:"2025-09-01", status:"active" },
      { name:"顺达汽修厂",   contact:"赵明",   phone:"137****3456", total:32400.00, reg_date:"2025-04-10", status:"active" },
      { name:"捷诚汽车美容", contact:"陈静",   phone:"158****7890", total:5200.00,  reg_date:"2025-11-20", status:"inactive" },
    ];
  },
  emptyList: [],
};
