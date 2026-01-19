-spec max_side_length(Mat :: [[integer()]], Threshold :: integer()) -> integer().
max_side_length(Mat, Threshold) ->
    Mat_ = mat_to_map(Mat),
    M = length(Mat),
    [Row | _] = Mat,
    N = length(Row),
    Prefix_Init = init_prefix_sum_map(M, N),
    Prefix_Sum = prefix_sum(Mat_, M, N, Prefix_Init),
    find_max_square(M, N, Prefix_Sum, Threshold).

mat_to_map(Mat) -> mat_to_map(Mat, 1, #{}).
mat_to_map([], _, Acc) -> Acc;
mat_to_map([Row | Rest], Y, Acc) -> mat_to_map(Rest, Y + 1, row_to_map(Row, Y, 1, Acc)).

row_to_map([], _, _, Acc) -> Acc;
row_to_map([E | Rest], Y, X, Acc) -> row_to_map(Rest, Y, X + 1, maps:put({Y,X}, E, Acc)).

init_prefix_sum_map(M, N) -> init_prefix_sum_map(M, N, 0, 0, #{}).
init_prefix_sum_map(M, _, Y, _, Acc) when Y > M -> Acc;
init_prefix_sum_map(M, N, Y, X, Acc) when X > N -> init_prefix_sum_map(M, N, Y + 1, 0, Acc);
init_prefix_sum_map(M, N, Y, X, Acc) -> init_prefix_sum_map(M, N, Y, X + 1, maps:put({Y, X}, 0, Acc)).

prefix_sum(Mat_, M, N, Acc) -> prefix_sum(Mat_, M, N, 1, Acc).
prefix_sum(_, M, _, Y, Acc) when Y > M -> Acc;
prefix_sum(Mat_, M, N, Y, Acc) -> prefix_sum(Mat_, M, N, Y + 1, prefix_sum_rowwise(Mat_, M, N, Y, 1, Acc)).

prefix_sum_rowwise(_, _, N, _, X, Acc) when X > N -> Acc;
prefix_sum_rowwise(Mat_, M, N, Y, X, Acc) ->
    Elem    = maps:get({Y, X}, Mat_, 0),
    SumUp   = maps:get({Y-1, X}, Acc, 0),
    SumLeft = maps:get({Y, X-1}, Acc, 0),
    SumDiag = maps:get({Y-1, X-1}, Acc, 0),
    PS = Elem + SumUp + SumLeft - SumDiag,
    prefix_sum_rowwise(Mat_, M, N, Y, X + 1, maps:put({Y, X}, PS, Acc)).

find_max_square(M, N, Prefix_Sum, Threshold) -> binary_search(0, min(M, N), M, N, Prefix_Sum, Threshold).

binary_search(Low, High, _, _, _, _) when Low >= High -> Low;
binary_search(Low, High, M, N, Prefix_Sum, Threshold) ->
    Mid = (Low + High + 1) div 2,
    case is_valid_square(Mid, M, N, Prefix_Sum, Threshold) of
        true -> binary_search(Mid, High, M, N, Prefix_Sum, Threshold);
        false -> binary_search(Low, Mid - 1, M, N, Prefix_Sum, Threshold)
    end.

is_valid_square(Side, M, N, Prefix_Sum, Threshold) when Side == 0 -> true;
is_valid_square(Side, M, N, Prefix_Sum, Threshold) ->
    lists:any(
        fun(Y) ->
            lists:any(
                fun(X) ->
                    Sum = maps:get({Y+Side-1, X+Side-1}, Prefix_Sum, 0)
                          - maps:get({Y-1, X+Side-1}, Prefix_Sum, 0)
                          - maps:get({Y+Side-1, X-1}, Prefix_Sum, 0)
                          + maps:get({Y-1, X-1}, Prefix_Sum, 0),
                    Sum =< Threshold
                end,
                lists:seq(1, N - Side + 1)
            )
        end,
        lists:seq(1, M - Side + 1)
    ).
