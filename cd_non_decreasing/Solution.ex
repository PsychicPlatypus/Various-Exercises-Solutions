defmodule TidyNumber do
  @spec tidy_number(integer) :: boolean()
  def tidy_number(n) do
    n |> to_char_list ==
      n
      |> to_char_list
      |> Enum.sort()
  end
end
