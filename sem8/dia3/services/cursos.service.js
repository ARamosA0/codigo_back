const MysqlLib = require('../lib/mysql');

class CursoService {

    constructor() {
        this.sql = new MysqlLib();
    }

    async getAll() {
        const sqlAll = "select * from tbl_curso";
        const result = await this.sql.querySql(sqlAll);
        return result;
    }

    async getById(id) {
        const sqlGetById = `select * from tbl_curso where curso_id = ${id}`;

        const result = await this.sql.querySql(sqlGetById);
        return result;
    }

}

module.exports = CursoService;