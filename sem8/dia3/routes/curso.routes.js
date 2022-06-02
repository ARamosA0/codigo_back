const express = require('express');
const CursoService = require('../services/cursos.service');

function cursoApi(app) {
    const router = express.Router();
    app.use("/curso", router);

    const objCursoService = new CursoService();

    router.get("/", async function(req, res) {
        try {
            const curso = await objCursoService.getAll();
            res.status(200).json({
                status: true,
                content: curso
            })
        } catch (err) {
            console.log(err)
        }
    })

    router.get("/:id", async function(req, res) {
        const { id } = req.params;
        try {
            const curso = await objCursoService.getById(id);
            if (curso.length > 0) {
                res.status(200).json({
                    status: true,
                    content: curso
                })
            } else {
                res.status(204).json({
                    status: true,
                    content: "no content"
                })
            }
        } catch (err) {
            console.error(err)
        }
    })
}

module.exports = cursoApi;