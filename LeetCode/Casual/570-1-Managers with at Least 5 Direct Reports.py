# https://leetcode-cn.com/problems/managers-with-at-least-5-direct-reports/
# 方法：使用临时表进行连接
# 算法：

# 首先，我们只需使用此 ManagerId 列就可以获取拥有 5 个以上直接下属的经理的 ID。
# 然后，我们可以通过将该表与 Employee 表连接来获取该经理的名称。
'''
SELECT
    Name
FROM
    Employee AS t1 JOIN
    (SELECT
        ManagerId
    FROM
        Employee
    GROUP BY ManagerId
    HAVING COUNT(ManagerId) >= 5) AS t2
    ON t1.Id = t2.ManagerId
;
'''
import pprint

# input_data = {"headers": {"Employee": ["Id", "Name", "Department", "ManagerId"]}, "rows": {"Employee": [[101, "John", "A", null],[102, "Dan", "A", 101], [103, "James", "A", 101], [104, "Amy", "A", 101], [105, "Anne", "A", 101], [106, "Ron", "B", 101]]}}
input_data = {
    "headers": {
        "Employee": ["Id", "Name", "Department", "ManagerId"]
    },
    "rows": {
        "Employee": [[101, "John", "A", None], [102, "Dan", "A", 101],
                     [103, "James", "A", 101], [104, "Amy", "A", 101],
                     [105, "Anne", "A", 101], [106, "Ron", "B", 101]]
    }
}
pprint.pprint(input_data)
