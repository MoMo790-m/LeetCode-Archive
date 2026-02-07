function* fibGenerator(): Generator<number, any, number> {
    let prev = 0;
    let curr = 1;

    yield prev; // 0
    yield curr; // 1

    while (true) {
        const next = prev + curr;
        yield next;
        prev = curr;
        curr = next;
    }
}
