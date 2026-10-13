Merge Queue Lab

This lightweight check validates merge queue mechanics only. It does not build
or test BlueOS. Full PR CI remains disabled in this experimental repository.

The required check runs on pull_request and merge_group and checks lower <= upper.
Baseline: lower.txt = 0, upper.txt = 10.
To reproduce the stale-green case, create two PRs from the same baseline:
A changes lower to 7; B changes upper to 5. Both pass separately.
Merge A through the queue, then enqueue the unchanged B. Its queue check fails.
Change B upper to 9 after dequeueing; it can then pass without rebasing.

The main ruleset requires merge commits, one queue build and one merge at a time.
Never update a queued sync PR branch: dequeue it or wait for it to leave first.
Keep experiment/mq-runtime-917339db in vivoblueos-lab/josh-sync while callers
pin 917339db32f1c1923409c0a3114d9167687873ab; it restores workflow reachability.
