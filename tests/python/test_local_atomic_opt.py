import taichi as ti
from tests import test_utils


@test_utils.test()
def test_cse():
    A = ti.field(ti.f32, shape=())

    @ti.kernel
    def func():
        a = 0
        a += 10
        a = a + 123
        A[None] = a

    func()
    assert A[None] == 133


@test_utils.test()
def test_store_forward():
    A = ti.field(ti.f32, shape=())

    @ti.kernel
    def func():
        a = 0
        a = 123
        a += 10
        A[None] = a

    func()
    assert A[None] == 133
